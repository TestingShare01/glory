# -*-encoding:utf-8 -*-
from glory import models
from logzero import logger
from glory.utils.Common.tools import *
# 获取case运行num次数
def getCaseRunNum(caseid,add=None):
    runCaseNum = models.caseapi.objects.filter(id=caseid)
    if add:
        runCaseNum.update(runCaseNum=int(runCaseNum[0].runCaseNum)+1)
    return runCaseNum[0].runCaseNum


# 运行log存储
def logModel(caseid,runNumId,msg):
    models.logCase.objects.create(caseid=caseid,runCaseNumId=runNumId,msg=msg)

# 获取任务环境配置通过域名返回IP
def retIp(envId,url):
    """
    envId:环境envId
    url:url地址
    """
    urls = url.split("/")
    env_id = models.environment.objects.filter(id=envId)[0].id
    ip = models.environment.objects.filter(envId=env_id,urlName=urls[2])
    if ip:
        url = urls[0]+"//"+ip[0].ip+"/"+"/".join(urls[3:])
        return url
    return url

# 推送未读消息
def sendMessage(name,type,user,typeId):
    """
    name:展示名称
    type:展示类型 目前只有api
    user：用户
    typeid：报告详情id
    """
    models.message.objects.create(name=name,type=type,mesId=typeId,userId=user,ifRead=0)

# 点击变已读消息
def clickMessage(id):
    models.message.objects.filter(id=id).update(ifRead=1)

# 根据caseid返回环境配置名称
def ret_task_env_name(caseid):
    res = models.Task.objects.filter(id=caseid)[0].env
    name = models.environment.objects.filter(id=res)[0].name
    logger.info(name)
    return name

# 统计数量+1
def statistical(types,getNum=None):
    """
    type指定类型，统计数量+1
    """
    typeif = models.statistical.objects.filter(type=types)

    setNum = 1
    if getNum !=None:
        setNum = getNum
    if typeif:
        nums = int(typeif[0].num) + setNum
        typeif.update(num=nums)
    else:
        models.statistical.objects.create(type=types, num=setNum)

