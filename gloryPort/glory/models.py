from django.db import models

# Create your models here.

class project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300,verbose_name="项目名称")
    describe = models.CharField(max_length=500,verbose_name="描述")
    jk_num = models.IntegerField(verbose_name="接口数量",default=0)
    case_num = models.IntegerField(verbose_name="用例数量",default=0)
    updatetime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table = "project"

class modelse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300,verbose_name="模块名称")
    project_id = models.CharField(max_length=100,verbose_name="关联项目id")
    describe = models.CharField(max_length=500,verbose_name="描述")
    jk_num = models.IntegerField(verbose_name="接口数量",default=0)
    case_num = models.IntegerField(verbose_name="用例数量",default=0)
    updatetime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table = "modelse"