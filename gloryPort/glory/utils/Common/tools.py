# -*-encoding:utf-8 -*-
import requests
from logzero import logger
import json
from glory import models
import re
from datetime import datetime
from glory.utils.Common.methods import *
from glory.utils.Common.methods import filterData
from glory.utils.Common.SaveModel import *
from glory.models import gloadConfig

import time
# 封装request
class Request:
    def post(self,url,datas,header):
        try:
            data = json.dumps(datas)
            res = requests.post(url,data=data,headers=header,verify=False)
            status = res.status_code
            res = res.content.decode("utf-8")
            try:
                return {"code": 0, "response": json.loads(res), "msg": status}
            except Exception as e:
                return {"code": 2, "response": res, "msg": status}
        except Exception as e:
            return {"code": 1, "msg": "{}".format(e), "res": e}

    def get(self,url,params,header,cookies):
        try:
            res = requests.get(url, params=params, headers=header,cookies=cookies,timeout=3000,verify=False)
            status = res.status_code
            tt = res.elapsed.microseconds
            res = res.content.decode("utf-8")
            try:
                return {"code":0,"response":json.loads(res),"msg":status}
            except Exception as e:
                return {"code":2,"response":res,"msg":status}
        except Exception as e :
            return {"code":1,"msg":"{}".format(e),"res":e}

    def seletMethod(self,method,url,data=None,header=None,cookies=None):
        if method == "POST":
            return self.post(url,data,header)
        else:
            return self.get(url,data,header,cookies)

# 获取json中数据
def analysis(rule,res):
    """
        value：json数据
        rule：获取的规则，层级多可写成 data.namelist.codeid的形式，支持列表的形式data.namelist[1].codeid

    """
    datas = rule.split(".")
    try:
        for i in datas:
            if "[" in i:
                index = i.index("[")
                keys = i[:index]
                num = int(i[index+1])
                res = res[keys][num]
            else:
                res = res[i]
        return {"status":0,"value":res,"msg":"获取值成功"}
    except Exception as e:
        return {"status":1,"value":101,"msg":"解析返回json失败:{}".format(e)}

# 返回结果与预期对比
def resultData(datajson,res):
    """datajson：请求返回的json数据
       res: 前端返回的验证数据
    """

    for i in res:
        if i["keys"] =="":
            return None
        resultcase = analysis(i["keys"],datajson)

        if resultcase["status"] == 0:
            i["result"] = resultcase["value"]
            if str(resultcase["value"]) == i["expect"]:
                i["status"] = 1    # 预期与实际结果一致返回1
            else:
                i["status"] = 2
        else:
            i["result"] = resultcase["msg"]
            i["status"] = 2
    return res

# 执行任务
def zxCase(data,taskId,user,taskName):
    """
    data:列表数据，包含object格式用例
    taskId:任务id
    user：执行人
    taskName:任务名称
    """
    # Case执行，返回执行结果数据格式如下
    # {{name:"case1",status:"成功",result:"1=1",caseId:5，res:response},{name:"case2",status:"失败",result:"1=13",caseId:10,res:response}}
    resultCase=[]
    info = {"num":0,"true_num":0,"false_num":0}
    if_gload = False #是否全局
    body = {}
    cookie = {}
    head = {}
    report_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    start_time = time.time()
    firstCase = models.gloadConfig.objects.filter(taskId=taskId,parameter="caseId")
    envs = models.Task.objects.filter(id=taskId)[0].env #envId
    envName = models.environment.objects.filter(id=envs)[0].name

    # 前置执行的Case
    if firstCase:
        for i in firstCase:
            oneCaseExecute(i.value,envs)
            # 前置cookie和headers

    if taskId:
        if getCookieGload(taskId, envName):
            logger.info("有全局内容")
            cookie = getCookieGload(taskId, envName)
            if_gload = True
        if getHeaderGload(taskId, envName):
            head = getHeaderGload(taskId, envName)

    if user:
        pass
    else:
        user=""
    logger.info(cookie)

    for i in data:
        info["num"]+=1
        case = {}
        case["name"] = i.name
        case["caseId"] = i.id
        caseid = i.id
        url = i.url
        methods = i.methods
        bodys = eval(i.bodys)
        cookies = eval(i.cookie)
        headers = eval(i.headers)
        result = eval(i.resultPk)

        # 配置执行环境
        if envs != "":
            url = retIp(envs, url)
        envName = models.environment.objects.filter(id=envs)[0].name

        if len(bodys) == 1:
            if bodys[0]["keys"] == "":
                body = None
            else:
                for i in bodys:
                    body[i["keys"]] = filterData(i["val"],envName)
        else:
            for i in bodys:
                body[i["keys"]] = filterData(i["val"],envName)

        if if_gload == False:
            logger.info("没有全局")
            for c in cookies:
                if c["keys"]=="":
                    cookie =None
                else:
                    cookie[c["keys"]] =filterData(c["val"],envName)

            for h in headers:
                if h["keys"] == "":
                    head = None
                else:
                    head[h["keys"]] = str(filterData(h["val"],envName))

        if case["caseId"]:
            getCaseRunNums = getCaseRunNum(case["caseId"],1)


        logModel(caseid=case["caseId"],runNumId=getCaseRunNums,msg="URL:{}".format(url))
        logModel(caseid=case["caseId"],runNumId=getCaseRunNums,msg="body:{},headers:{},cookies:{}".format(body,head,cookie))
        api_case_start_time = time.time()
        res = Request().seletMethod(methods,url,body,head,cookie)
        api_case_end_time = time.time()
        api_case_expent_time = round((api_case_end_time-api_case_start_time)*1000)
        case["expent_time"] = api_case_expent_time
        logModel(caseid=case["caseId"],runNumId=getCaseRunNums,msg=res)

        # 获取返回结果与预期结果对比
        if res["code"] == 1:   # 返回code=1，请求就失败了
            info["false_num"]+=1
            case["status"] = "失败"
            case["result"] = res["msg"]
            case["response"] = "返回数据报错，报错问题：{}".format(res["msg"])
        elif res["code"] == 2:
            if res["msg"] == 200:
                info["true_num"] += 1
                case["status"] = "成功"
                case["result"] = "状态码200"
                case["response"] = res["response"]
            else:
                info["false_num"] += 1
                case["status"] = "失败"
                case["result"] = res["msg"]
                case["response"] = "返回数据报错，报错问题：{}".format(res["msg"])

        else:
            case["response"] = res["response"]
            if result[0]["keys"] == "":   # 没有预期值的话，就判断状态码200就算正确
                if res["msg"] ==200:
                    info["true_num"] += 1
                    case["status"] = "成功"
                    case["result"] = "状态码200"
                    case["response"] = res["response"]

                else:
                    info["false_num"] += 1
                    case["status"] = "失败"
                    case["result"] = res["msg"]
            else:   # 存在多个预期值，全部都对的情况，才算正确
                res_yq = resultData(res["response"],result)
                ifStatus = "成功"
                str_result = ""
                for i in res_yq:
                    if i["status"] == 2:
                        ifStatus = "失败"
                        str_result = str_result + "预期:{} != 实际:{};".format(i["expect"],i["result"])
                    else:
                        str_result = str_result + "预期:{} = 实际:{};".format(i["expect"],i["result"])
                case["status"] = ifStatus
                case["result"] = str_result
                if ifStatus =="成功":
                    info["true_num"]+=1
                else:
                    info["false_num"] += 1

        # 提取器部分

        extractor(caseid,envName,res)


        resultCase.append(case)
    accuracy = "{:.0f}%".format(info["true_num"]/info["num"]*100)
    end_time = time.time()
    spent = end_time - start_time
    m,s  = divmod(spent,60)
    spent = "{}分{}秒".format(str(m).split(".")[0],str(s).split(".")[0])
    report_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    obj = models.Report.objects.create(zx_user=user,task_num=taskName,taskId=taskId,num=info["num"],api_num=info["num"],case_num=0,true_num=info["true_num"],false_num=info["false_num"],accuracy=accuracy,expend_time=spent,createtime=datetime.now(),start_time=report_start_time,end_time=report_end_time)
    statistical("report")
    statistical("apiNum",info["num"])
    statistical("trueApi",info["true_num"])
    statistical("falseApi",info["false_num"])
    for i in resultCase:
        logger.info(i)
        models.CaseResult.objects.create(reportId=obj.id,name=i["name"],result=i['result'],status=i["status"],res=i["response"],caseid=i["caseId"],expent_time=i["expent_time"])
    taskNum = models.Task.objects.filter(id=taskId)
    sendMessage("接口任务#{}".format(obj.id),"api",user,obj.id)
    taskNum.update(zx_num = int(taskNum[0].zx_num)+1,status="未执行",accuracy=accuracy)

# 定时任务执行
def getCaseList(id):

    obj = models.Task.objects.filter(id=id)
    obj.update(status="执行中",zx_time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),user="定时任务")

    username = obj[0].name

    obj = obj[0].id_list
    id_list = eval(obj)
    infos = models.caseapi.objects.filter(id__in=id_list)
    zxCase(infos, id,"定时任务",username)

# 任务全局Cookie
def getCookieGload(taskid,envName):
    date={"taskId":taskid,"parameter":"cookies",}
    data = gloadConfig.objects.filter(**date)
    cook = {}
    if data:
        for i in eval(data[0].value):
            cook[i["keys"]] = filterData(i["val"],envName)
        return cook
    else:
        return None

# 任务全局Headers
def getHeaderGload(taskid,envName):
    date = {"taskId": taskid, "parameter": "headers"}
    data = gloadConfig.objects.filter(**date)
    head = {}
    if data:
        for i in eval(data[0].value):
            head[i["keys"]] = filterData(i["val"],envName)
        return head
    else:
        return None

# 单接口请求返回数据
def oneCaseExecute(caseId,envId=None):
    """
    caseId：用例ID
    envId：环境ID
    """
    case = models.caseapi.objects.filter(id=caseId)[0]
    envName = None
    if envId:
        envName = models.environment.objects.filter(id=envId)[0].name

    if case:
        url = case.url
        method = case.methods
        bodys = eval(case.bodys)
        cookies = eval(case.cookie)
        headers = eval(case.headers)
        result = eval(case.resultPk)
        body = {}
        cookie ={}
        head = {}
        if len(bodys) == 1:
            if bodys[0]["keys"] == "":
                body = None
            else:
                for i in bodys:
                    body[i["keys"]] = filterData(i["val"],envName)
        else:
            for i in bodys:
                body[i["keys"]] = filterData(i["val"],envName)

        for c in cookies:
            if c["keys"]=="":
                cookie =None
            else:
                cookie[c["keys"]] =filterData(c["val"],envName)

        for h in headers:
            if h["keys"] == "":
                head = None
            else:
                head[h["keys"]] = str(filterData(h["val"],envName))
        envName = ""
        if envId:
            url = retIp(envId, url)
            envName = models.environment.objects.filter(id=envId)[0].name
        res = Request().seletMethod(method,url,body,head,cookie)
        extractor(caseId,envName,res)

# 分页功能
from rest_framework.pagination import PageNumberPagination

class MyPage(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    max_page_size = 40

    def setting_page(self, queryset, request, view=None):
        list_data = self.paginate_queryset(queryset, request,self)
        count_data = self.django_paginator_class(queryset,1).count
        return {"list_data":list_data,"count_data":count_data}


# 提取器，获取case中的字段，赋值后写入全局中
def extractor(caseid,envName,res):
    """
    caseid:用例ID
    envName: 环境名称
    """
    env_data = models.gloadCaseKey.objects.filter(caseid=caseid,env=envName)
    if env_data:
        env_data.delete()
    tiqu_list = models.caseapi.objects.filter(id=caseid)[0].extractor
    if tiqu_list !="":
        tiqu_list = eval(tiqu_list)
        for i in tiqu_list:
            keyRule = i["keyRule"]
            keyName = i["keyName"]
            try:
                val = analysis(keyRule,res["response"])
                if val["status"] == 0:
                    values = val["value"]
                else:
                    values = "提取结果失败caseID:{}".format(caseid)
            except:
                values = "返回数据无法提取caseID:{}，接口返回数据:{}".format(caseid,res)
            models.gloadCaseKey.objects.create(caseid=caseid,keyRule=keyRule,keyName=keyName,values=values,env=envName)