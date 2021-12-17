from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from glory import models
from logzero import logger
from glory import Serializer

#创建项目
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
            models_list = models.modelse.objects.filter(project_id=projectId)
            logger.info(models_list)
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
            logger.info(project_id)
            models.modelse.objects.create(name=name, describe=describe,project_id=project_id)
            ret["code"] = 0
            ret["msg"] = "创建成功"
        except Exception as e:
            ret["code"] = 1
            ret["msg"] = "创建失败:{}".format(e)
        return Response(ret)


