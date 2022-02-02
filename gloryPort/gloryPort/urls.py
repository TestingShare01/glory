"""gloryPort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from glory.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("teacher",teacher.as_view()),
    path("project",project.as_view()),
    path("modelss",modelss.as_view()),
    path("jkCase",jkCase.as_view()),
    path("jkSave",jkCaseSave.as_view()),
    path("tag",tag.as_view()),
    path("task",task.as_view()),
    path("zxTaskCase",zx_task_case.as_view()),
    path("reportInfo",reportInfo.as_view()),
    path("timetask",timetask.as_view()),
    path("reportDetail",reportDetail.as_view()),
    path("caseLogInfo",caseLogInfo.as_view()),
    path("Login",Login.as_view()),
    path("testList",testList.as_view()),
    path("getNum",getNum.as_view()),
    path("gloabs",gloabs.as_view()),
    path("variable",variable.as_view()),
    path("envSetting",envSetting.as_view()),
    path("urlAdd",urlAdd.as_view())
]
