# -*-encoding:utf-8 -*-
import requests

class Request:
    def post(self,url,datas,header):
        try:
            res = requests.post(url,data=datas,headers=header)
            status = res.status_code
            res = res.content
            return {"code":0,"response":res,"msg":status}
        except Exception as e :
            return {"code":1,"msg":e}

    def get(self,url,params,header):
        try:
            res = requests.get(url,params=params,headers=header)
            status = res.status_code
            res = res.content
            return {"code":0,"response":res,"msg":status}
        except Exception as e :
            return {"code":1,"msg":e}

    def seletMethod(self,method,url,data,header):
        if method == "POST":
            self.post(url,data,header)
        else:
            self.get(url,data,header)