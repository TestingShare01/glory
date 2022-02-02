# -*-encoding:utf-8 -*-
from logzero import logger
from glory import models

def time():
    return 2211332


time = time()
# 过滤请求参数，是否存在变量
def filterData(data,envName=None):
    if "$" in data:
        vals = data[1:]
        logger.info(vals)
        if envName:
            val = models.gloadCaseKey.objects.filter(keyName=vals,env=envName)
            if val:
                return val[0].values
            return vals
    else:
        return data
