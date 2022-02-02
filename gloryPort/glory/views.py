from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from glory import models
from logzero import logger
from glory import Serializer
from glory.utils.Common.tools import Request,analysis,resultData,zxCase,getCaseList,MyPage,extractor
from glory.utils.Common.methods import filterData
from glory.utils.Common.SaveModel import *
from glory.utils.Common.tools import Request
from datetime import datetime
import time
import json
from apscheduler.schedulers.background import BackgroundScheduler
from multiprocessing import Process

from rest_framework.generics import ListCreateAPIView


mypage = MyPage()

class Login(APIView):
    def post(self,req,*args,**kwargs):
        ret = {}
        userName = ""
        user = req.data.get("user")
        pwd = req.data.get("pwd")
        user = models.User.objects.filter(user=user)
        if user:
            logger.info(user[0].pwd)
            if user[0].pwd == pwd:
                code = 0
                msg = "登录成功"
                userName  = user[0].user
            else:
                code = 1
                msg = "密码错误"
        else:
            code = 1
            msg = "账号不存在"
        ret["code"] = code
        ret["msg"] = msg
        ret["user"] = userName
        return Response(ret)

    def get(self,req,*args):
        ret = {}
        user = req.query_params.get("user")
        pwd = req.query_params.get("pwd")
        logger.info(user)
        logger.info(pwd)
        users = models.User.objects.filter(user=user)
        logger.info(users)
        if users:
            code = 1
            msg = "用户名已存在"
        else:
            models.User.objects.create(user=user,pwd=pwd)
            code = 0
            msg = "注册成功"
        ret["code"] = code
        ret["msg"] = msg
        return Response(ret)

#创建项目
scheduler = BackgroundScheduler(timezone='Asia/Shanghai')

class project(APIView):
    def post(self,req,*args,**kwargs):
        """创建项目"""
        ret = {}
        try:
            name = req.data.get("name")
            describe = req.data.get("describe")
            models.project.objects.create(name=name,describe=describe)
            ret["code"] = 0
            ret["msg"] = "创建成功"
        except Exception as e:
            ret["code"] = 1
            ret["msg"] = "创建失败:{}".format(e)
        return Response(ret)

    def get(self,req,*args,**kwargs):
        ret={}
        try:
            project_list = models.project.objects.all()
            project_list = Serializer.projectSerializer(project_list,many=True)
            ret["code"] = 0
            ret["data"] = project_list.data
            ret["msg"] = "获取数据成功"
        except Exception as e:
            ret["code"] = 1
            ret["data"] = []
            ret["msg"] = "获取失败：{}".format(e)
        return Response(ret)

# 创建模块
class modelss(APIView):
    def get(self,req,*args,**kwargs):
        ret = {}
        try:
            projectId = req.query_params.get("id")
            if projectId:
                models_list = models.modelse.objects.filter(project_id=projectId)
            else:
                models_list = models.modelse.objects.all()

            models_list = Serializer.modelSerializer(models_list, many=True)
            ret["code"] = 0
            ret["data"] = models_list.data
            ret["msg"] = "获取数据成功"

        except Exception as e:
            ret["code"] = 1
            ret["data"] = []
            ret["msg"] = "获取失败：{}".format(e)
        return Response(ret)

    def post(self,req,*args,**kwargs):
        ret = {}
        try:
            name = req.data.get("name")
            describe = req.data.get("describe")
            project_id = req.data.get("projectId")
            models.modelse.objects.create(name=name, describe=describe,project_id=project_id)
            ret["code"] = 0
            ret["msg"] = "创建成功"
        except Exception as e:
            ret["code"] = 1
            ret["msg"] = "创建失败:{}".format(e)
        return Response(ret)


# 单接口请求
class jkCase(APIView):
    def post(self,req,*args,**kwargs):
        caseid = req.data.get("id")
        method = req.data.get("method")
        url = req.data.get("url")
        data = req.data.get("datas")
        result = req.data.get("result")
        headers = req.data.get("headers")
        cookies = req.data.get("cookies")
        logger.info(data)
        parames = {}
        head = {}
        cookie = {}
        if caseid:
            runNum = int(getCaseRunNum(caseid))+1
        if data[0]["keys"]=="":
            parames = None
        else:
            for i in data:
                parames[i["keys"]] = filterData(i["val"])
        for i in headers:
            head[i["keys"]] = str(filterData(i["val"]))
        if len(head) == 1:
            head = None
        if cookies:
            if cookies[0]["keys"] == "":
                cookie = None
            else:
                for j in cookies:
                    cookie[j["keys"]] = filterData(j["val"])
        res = Request().seletMethod(method,url,parames,head,cookie) # 返回数据与预期结果对比，如果code=1的话，就没有response数据报错，需要兼容
        if caseid:
            logModel(caseid,runNum,"data:{}".format(parames))
            logModel(caseid,runNum,"headers:{}".format(head))
            logModel(caseid,runNum,"cookies:{}".format(cookie))

            logModel(caseid,runNum,"返回结果:{}".format(res))
            getCaseRunNum(caseid,1)
        if res["code"] == 0:
            result = resultData(res["response"],result)
            if result:
                logModel(caseid, runNum, "断言数据:{}".format(result))

            extractor(caseid, "单接口调试", res)

            return Response({"res": res, "result": result})

        else:
            return Response({"res": res, "result":0})
    def get(self,req,*args,**kwargs):
        id = req.query_params.get("id")
        obj = models.caseapi.objects.filter(id=id)
        if obj:
            obj.delete()
        else:
            return Response("未找到")
        return Response("删除成功")

# 保存接口，获取接口
class jkCaseSave(APIView):
    def post(self,req,*args,**kwargs):
        id = req.data.get("id") #获取id
        name = req.data.get("name") #名称
        user = req.data.get("user") # 用户名
        remark = req.data.get("remark") #备注
        priority = req.data.get("priority") #优先级
        mokuai = req.data.get("mokuai") # 所属模块
        tag = req.data.get("tag") #标签
        url = req.data.get("url") # url
        selectmethod = req.data.get("selectmethod")
        bodys = req.data.get("datas") # bodys
        headers = req.data.get("headers") # headers
        cookies = req.data.get("cookies") #cookie
        resultPk = req.data.get("resultPk") # 断言
        for i in tag:
            tagObj = models.Tag.objects.filter(name=i)
            if tagObj:
                pass
            else:
                models.Tag.objects.create(name=i)
        logger.info(user)
        if id:
            obj = models.caseapi.objects.filter(id=id)
            obj.update(name=name,remark=remark,priority=priority,mokuai=mokuai,tag=tag,url=url,methods=selectmethod,bodys=bodys,headers=headers,cookie=cookies,resultPk=resultPk,updatetime=datetime.now(),user=user)
        else:
            mk = models.modelse.objects.filter(name=mokuai)

            models.caseapi.objects.create(name=name,remark=remark,priority=priority,mokuai=mokuai,tag=tag,url=url,methods=selectmethod,bodys=bodys,headers=headers,cookie=cookies,resultPk=resultPk,user=user)

        return Response(111)

    def get(self,req,*args,**kwargs):
        id = req.query_params.get("id")
        tag = req.query_params.get("tag")
        mokuai = req.query_params.get("mokuai")
        priority = req.query_params.get("priority")
        select = req.query_params.get("select")
        ret = {}
        sel = {}
        if select:
            if tag:
                sel["tag"] = "['{}']".format(tag)
            if mokuai:
                sel["mokuai"] = mokuai
            if priority:
                sel["priority"] = priority
            api_list = models.caseapi.objects.filter(**sel)
        else:
            if id:
                api_list = models.caseapi.objects.filter(id=id)
                tiqu_list = models.gloadCaseKey.objects.filter(caseid=id)
                tiqu_list = Serializer.gloabKeySerializer(tiqu_list,many=True)
                ret["tiqu_list"] = tiqu_list.data
            else:
                api_list = models.caseapi.objects.all()
        data_list = mypage.setting_page(api_list,req,self)
        api_list = Serializer.apiSerializer(data_list["list_data"], many=True)
        ret["api_list"] = api_list.data
        ret["countNum"] = data_list["count_data"]
        ret["code"] = 0
        return Response(ret)

# 添加新标签，获取全部标签
class tag(APIView):
    def get(self,req,*args,**kwargs):
        tag_list = models.Tag.objects.all()
        tag_list = Serializer.tagSerializer(tag_list,many=True)
        return Response(tag_list.data)

# 创建任务，获取任务
class task(APIView):
    def post(self,req,*args,**kwargs):
        ret={}
        try:
            id = req.data.get("id_list")
            name = req.data.get("name")
            username = req.data.get("username")
            num = len(id)
            ifname = models.Task.objects.filter(name=name)
            if ifname:
                ret["code"] = 1
                ret["msg"] = "任务名已存在"
            else:
                models.Task.objects.create(id_list=id,name=name,api_num=num,case_num = 0,zx_num=0,status="未执行",makeUser=username)
                ret["code"] = 0
                ret["msg"] ="创建成功"
        except Exception as e:
            ret["code"] = 1001
            ret["msg"] = "接口报错:{}".format(e)
        return Response(ret)

    def get(self,req,*args,**kwargs):
        id = req.query_params.get("id")
        if id:
            pass
        else:
            task_list = models.Task.objects.all()
            task_list = Serializer.taskSerializer(task_list,many=True)
            return Response(task_list.data)

# 执行任务
class zx_task_case(APIView):
    def post(self,req,*args,**kwargs):
        id = req.data.get("id")
        userName = req.data.get("user")
        obj = models.Task.objects.filter(id=id)[0]
        taskName = obj.name
        obj = obj.id_list
        id_list = eval(obj)
        logger.info(userName)
        infos = models.caseapi.objects.filter(id__in=id_list)
        models.Task.objects.filter(id=id).update(status="执行中",zx_time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),user=userName)
        p = Process(target=zxCase,args=(infos,id,userName,taskName,))
        p.run()
        logger.info("主进程进行中。..。。。。。。。。。。")
        return Response(1111)

    def get(self,req,*args,**kwargs):
        id = req.query_params.get("id")
        logger.info(id)
        models.Task.objects.filter(id=id).delete()
        return Response("删除成功")

# 报告列表
class reportInfo(APIView):
    def get(self,req,*args,**kwargs):
        ret={}
        try:
            taskId = req.query_params.get("id")
            if taskId:
                report_list = models.Report.objects.filter(taskId=taskId).order_by("-id")
            else:
                report_list = models.Report.objects.all().order_by("-id")
            ret_data = mypage.setting_page(report_list, req)
            report_list = Serializer.reportSerializer(ret_data["list_data"],many=True)
            num_list = models.statistical.objects.all()
            num_list = Serializer.statisticalSerializer(num_list,many=True)
            ret["num_list"] = num_list.data
            ret["data_list"] = report_list.data
            ret["code"] = 0
            ret["countNum"] = ret_data["count_data"]
            return Response(ret)
        except Exception as e:
            logger.info(e)
            ret["code"] = 1001
            ret["msg"] = "接口报错:{}".format(e)
            return Response(ret)


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
jobstores = {
    # 'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///db.sqlite3')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

schedulers = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults,
                                 timezone='Asia/Shanghai')


from apscheduler.triggers.cron import CronTrigger

schedulers.start()
logger.info("start~~~~~")
# 定时任务
class timetask(APIView):
    def post(self,req,*args,**kwargs):
        id = req.data.get("id")
        cron = req.data.get("cron")
        try:
            schedulers.add_job(getCaseList,trigger=CronTrigger.from_crontab(cron,timezone='Asia/Shanghai'),id=str(id),args=['{}'.format(id)],coalesce=True)
            models.Task.objects.filter(id=id).update(cron=cron)

        except Exception as e:
            if "conflicts with an existing job" in str(e):
                schedulers.remove_job(str(id))
                schedulers.add_job(getCaseList, trigger=CronTrigger.from_crontab(cron, timezone='Asia/Shanghai'),
                                   id=str(id), args=['{}'.format(id)], coalesce=True)
                models.Task.objects.filter(id=id).update(cron=cron)
        schedulers.start()
        return Response(11111)

    def get(self,req):
        id = req.query_params.get("id")
        logger.info(id)
        schedulers.remove_job(str(id))
        models.Task.objects.filter(id=id).update(cron="")
        return Response(222)

# 报告详情
class reportDetail(APIView):
    def get(self,req,*args,**kwargs):
        detail = req.query_params.get("id")
        detail_list = models.CaseResult.objects.filter(reportId=detail)
        detail_list = Serializer.detailSerializer(detail_list,many=True)
        info = models.Report.objects.filter(id=detail)
        info = Serializer.reportSerializer(info,many=True)
        return Response({"reportList":detail_list.data,"info":info.data})

# 日志log
class caseLogInfo(ListCreateAPIView):
    def get(self,req):
        caseid = req.query_params.get("id")
        log_list = models.logCase.objects.filter(caseid=caseid).order_by("-createtime")[:30]
        log_list = Serializer.logSerializer(log_list,many=True)
        return Response(log_list.data)


# 首页总数量
class getNum(ListCreateAPIView):
    queryset = models.Num.objects.all()
    serializer_class = Serializer.numSerializer

# 全局任务配置
class gloabs(APIView):
    def post(self,req):
        taskId = req.data.get("taskId")
        parameter = req.data.get("parameter")
        val = req.data.get("values")
        if parameter == "env":
            models.Task.objects.filter(id=taskId).update(env=val)

        models.gloadConfig.objects.create(taskId=taskId,parameter=parameter,value=val)

        return Response("创建成功")

    def get(self,req):
        taskId = req.query_params.get("taskId")
        gloab_list = models.gloadConfig.objects.filter(taskId=taskId)
        envid = models.Task.objects.filter(id=taskId)[0].env
        env_name = models.environment.objects.filter(id=envid)[0].name
        gloab_list = Serializer.gloabSerializer(gloab_list,many=True)
        return Response({"gloab":gloab_list.data,"envid":env_name})


# 全局配置变量
class variable(APIView):
    def post(self,req):
        filterValue = {}
        caseId = req.data.get("caseId")
        tiquList = req.data.get("tiquList")

        if tiquList:
            logger.info(tiquList)
            models.caseapi.objects.filter(id=caseId).update(extractor=tiquList)
        return Response("全局变量保存成功")

    def get(self,req):
        list_gloab = models.gloadCaseKey.objects.all().order_by("-updatetime")
        list_gloab = Serializer.gloabKeySerializer(list_gloab,many=True)
        return Response(list_gloab.data)


# 环境配置
class envSetting(APIView):
    def post(self,req):
        name = req.data.get("envName")
        envId = req.data.get("envId")
        domain = req.data.get("domain")
        ip = req.data.get("ip")
        if name:
            models.environment.objects.create(name=name) #添加环境配置
        else:
            models.environment.objects.create(envId=envId,urlName=domain,ip=ip) #增加域名配置
        return Response("添加成功")

    def get(self,req):
        envId = req.query_params.get("envId")
        if envId:
            envIp_list = models.environment.objects.filter(envId=envId) #获取域名列表数据
        else:
            envIp_list = models.environment.objects.filter(envId="") # 获取环境数据

        envIp_list = Serializer.envSerializer(envIp_list,many=True)
        return Response(envIp_list.data)

# URL导入域名
class urlAdd(APIView):
    def post(self,req):
        envId = req.data.get("envId")
        url = req.data.get("url")
        logger.info(url)
        res = Request().seletMethod("GET",url)
        logger.info(str(res))
        if res["code"] !=1:
            rest = str(res["response"]).splitlines()
            logger.info(rest)
            for i in rest:
                if i !="":
                    pass
                    models.environment.objects.create(envId=envId, urlName=i.split(" ")[1], ip=i.split(" ")[0])
        return Response(1111)

# test
class testList(ListCreateAPIView):
    # queryset = models.logCase.objects.all()
    serializer_class = Serializer.logSerializer

    def post(self,req):
        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


# 测试搜索
class teacher(APIView):
    def get(self,req):
        ip = models.environment.objects.filter(envId=647, urlName="jzx.aixuexi.com")
        logger.info(ip)
        return Response(111111)