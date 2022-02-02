from logzero import logger
import time

logger.info(111)

url= "https://www.aixuexi.com/surrogates/passport/user/login"

url = url.split("/")
# ip = models.environment.objects.filter(envId=envId,urlName=url[2])[0].ip
ip = "113.321.123.123"
URL = url[0]+"//"+ip+"/"+"/".join(url[3:])
logger.info(URL)