#coding=utf-8
__author__ = 'zhaolinhuang'
from weibo import APIClient
APP_KEY = '4028896591'
APP_SECRET = '0d2e086881289fc93e8cc520c9016343'
CALLBACK_URL = 'http://127.0.0.1:8000/createSinaWeiboSession.htm'

weiboSession=None
client=None
def getCodeUrl():
    global client
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    return client.get_authorize_url()

def setAccessToken(code):
    global weiboSession
    weiboSession=client.request_access_token(code)
    accessToken = weiboSession.access_token # 新浪返回的token，类似abc123xyz456
    expiresIn = weiboSession.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    # TODO: 在此可保存access token
    global client
    client.set_access_token(accessToken, expiresIn)

def searchUsers(uid,screenName=None):
    global client
    if uid:
        return client.users.show.get(uid=uid)
    else:
        users=client.users.show.get(screen_name=screenName)
        return users

