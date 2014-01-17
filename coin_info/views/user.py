__author__ = 'zhaolinhuang'
from django.shortcuts import render
from django.http import HttpResponse
from coin_info.exceptionCode import CoinfoException
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangoLogin
from django.contrib.auth import get_user
from coin_info.log import log
import commonView
import json

def loginPage(request):
    return render(request,"user/login.html")


def login(request):
    username=None
    passwrod=None
    try:
        params=request.POST
        username=params.get("username",None)
        passwrod=params.get("password",None)
        loginUser=authenticate(username=username,password=passwrod)
        if loginUser and loginUser.is_active:
            djangoLogin(request, loginUser)
            return HttpResponse(json.dumps(commonView.reponseOK()))
        else:
            raise CoinfoException(CoinfoException.USER_PASSWORD_ERR)
    except Exception,e:
        log.error("LOGIN ERROR :%s:%s %s"%(username,passwrod,e))
        return HttpResponse(json.dumps(commonView.responseCommon(e)))




