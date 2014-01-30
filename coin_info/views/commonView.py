__author__ = 'zhaolinhuang'
from coin_info.exceptionCode import CoinfoException
from django.shortcuts import render
def responseCommonException(e):
    if isinstance(e,CoinfoException):
        message="%s"%e
        messageArr=message.split("-")
        return {"sysCode":messageArr[0],"message":messageArr[1]}
    else:
        return {"sysCode":"999999","message":"sys error!!"}

def reponseOK(code=0):
    return {"sysCode":code}

def http404(reqeust):
    return render(reqeust,"common/404.html")

def http500(reqeust):
    return render(reqeust,"common/500.html")
