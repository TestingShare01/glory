from django.db import models

# Create your models here.

# 项目
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

# 模块
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

# 接口
class caseapi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500,verbose_name="接口名称")
    remark = models.CharField(max_length=1000,verbose_name="备注",default="")
    priority = models.CharField(max_length=100,verbose_name="优先级")
    mokuai = models.CharField(max_length=300,verbose_name="所属模块")
    tag = models.CharField(max_length=200,verbose_name="所属标签")
    url = models.CharField(max_length=300,verbose_name="URL")
    methods = models.CharField(max_length=100,verbose_name="请求方法")
    bodys = models.CharField(max_length=1000,verbose_name="body",default=None)
    headers = models.CharField(max_length=1000,verbose_name="headers",default=None)
    cookie = models.CharField(max_length=1000,verbose_name="cookie",default=None)
    extractor = models.CharField(max_length=1000,verbose_name="提取器",default="")
    resultPk = models.CharField(max_length=1000,verbose_name="验证字段",default=None)
    user = models.CharField(max_length=300,verbose_name="添加人员",default="")
    runCaseNum = models.IntegerField(verbose_name="接口运行次数统计",default=0)
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "caseapi"

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=200,verbose_name="标签名称")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "tag"

# 任务
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300,verbose_name="任务名称")
    id_list = models.CharField(max_length=300,verbose_name="用例id")
    api_num = models.IntegerField(verbose_name="接口数量")
    case_num = models.IntegerField(verbose_name="用例数量")
    status = models.CharField(max_length=200,verbose_name="执行状态") # 0 未开始 1执行中
    user = models.CharField(max_length=200,verbose_name="执行者")
    makeUser = models.CharField(max_length=200,verbose_name="创建者",default="")
    zx_num = models.IntegerField(verbose_name="执行次数")
    cron = models.CharField(max_length=200,verbose_name="定时任务时间")
    accuracy = models.CharField(max_length=200,verbose_name="最新的正确率")
    zx_time = models.CharField(max_length=300,verbose_name="执行时间",default="")
    env = models.CharField(max_length=100,verbose_name="环境id",default="")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")


    class Meta:
        db_table = "Task"


# 报告统计数据列表展示
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    task_num = models.CharField(max_length=200,verbose_name="任务名",default="")
    zx_user = models.CharField(max_length=200,verbose_name="执行者")
    taskId = models.CharField(max_length=100,verbose_name="关联任务id")
    num = models.IntegerField(verbose_name="总数量")
    api_num = models.IntegerField(verbose_name="接口数量")
    case_num = models.IntegerField(verbose_name="用例数量")
    true_num = models.IntegerField(verbose_name="正确数")
    false_num = models.IntegerField(verbose_name="错误数")
    accuracy = models.CharField(max_length=100,verbose_name="正确率")
    start_time = models.CharField(max_length=200,verbose_name="开始时间",default="")
    end_time = models.CharField(max_length=200,verbose_name="结束时间",default="")
    expend_time = models.CharField(max_length=100,verbose_name="消耗时间",default=0)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "Report"

# 接口执行结果
class CaseResult(models.Model):
    id = models.AutoField(primary_key=True)
    reportId = models.CharField(max_length=100,verbose_name="关联报告id")
    name = models.CharField(max_length=300,verbose_name="用例名称")
    result = models.CharField(max_length=300,verbose_name="结果")
    status = models.CharField(max_length=500,verbose_name="状态")
    caseid = models.CharField(max_length=100,verbose_name="接口id")
    expent_time = models.CharField(max_length=300,verbose_name="消耗时间")
    res = models.CharField(max_length=2000,verbose_name="response")
    class Meta:
        db_table = "CaseResult"


class SchedlerModel(models.Model):
    id = models.AutoField(primary_key=True)
    funcName = models.CharField(max_length=300,verbose_name="方法名称")
    taskid = models.CharField(max_length=200,verbose_name="定时任务id")
    type = models.CharField(max_length=200,verbose_name="定时类型")
    tasktime = models.CharField(max_length=300,verbose_name="任务时间")
    args = models.CharField(max_length=300,verbose_name="参数")

    class Meta:
        db_table = "SchedlerModel"

class logCase(models.Model):
    id = models.AutoField(primary_key=True)
    caseid = models.IntegerField(verbose_name="caseid")
    runCaseNumId = models.IntegerField(verbose_name="运行次数id")
    msg = models.CharField(max_length=1000,verbose_name="执行日志内容")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "logCase"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=500,verbose_name="用户名")
    pwd = models.CharField(max_length=500,verbose_name="密码")
    token = models.CharField(max_length=1000,verbose_name="Token")
    role = models.CharField(max_length=500,verbose_name="角色",default=0)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "User"

class Num(models.Model):
    xiangmu = models.IntegerField(verbose_name="项目数")
    mokuai = models.IntegerField(verbose_name="模块数")
    taskNum = models.IntegerField(verbose_name="任务数量")
    taskexecute = models.IntegerField(verbose_name="任务执行次数")
    taskdingshi = models.IntegerField(verbose_name="任务执行定时次数")
    apiNum = models.IntegerField(verbose_name="接口数量")
    caseNum = models.IntegerField(verbose_name="用例数量")

    class Meta:
        db_table = "num"

class statistical(models.Model):
    type = models.CharField(max_length=200,verbose_name="统计类型")
    num = models.IntegerField(verbose_name="统计数量")

    class Meta:
        db_table = "statistical"

class gloadConfig(models.Model):
    taskId = models.CharField(max_length=100,verbose_name="任务id")
    parameter = models.CharField(max_length=200,verbose_name="参数")
    value = models.CharField(max_length=1000,verbose_name="值")

    class Meta:
        db_table = "gloadConfig"

class gloadCaseKey(models.Model):
    caseid = models.CharField(max_length=100,verbose_name="caseid")
    keyRule = models.CharField(max_length=200,verbose_name="提取规则")
    keyName = models.CharField(max_length=200,verbose_name="赋值参数")
    values = models.CharField(max_length=1000,verbose_name="提取值")
    env = models.CharField(max_length=100,verbose_name="执行环境",default="")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "gloadCaseKey"

class environment(models.Model):
    name = models.CharField(max_length=500,verbose_name="环境名称")
    envId = models.CharField(max_length=100,verbose_name="环境ID")
    urlName = models.CharField(max_length=300,verbose_name="域名")
    ip = models.CharField(max_length=200,verbose_name="ip")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "environment"

class message(models.Model):
    name = models.CharField(max_length=300,verbose_name="名称")
    type = models.CharField(max_length=100,verbose_name="通知类型")
    mesId = models.CharField(max_length=100,verbose_name="通知内容ID")
    userId = models.CharField(max_length=100,verbose_name="用户ID")
    ifRead = models.CharField(max_length=100,verbose_name="是否已读")
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "message"