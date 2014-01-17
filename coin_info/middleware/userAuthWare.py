__author__ = 'zhaolinhuang'
from django.shortcuts import render
from coin_info.views import user
class UserAuthWare(object):
    def process_request(self,request):
        if "login.htm" not in request.path and  "loginUser" not in request.session:
            return user.loginPage(request)
