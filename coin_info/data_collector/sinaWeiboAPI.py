#coding=utf-8
__author__ = 'zhaolinhuang'
from weibo import APIClient
APP_KEY = '4028896591'
APP_SECRET = '0d2e086881289fc93e8cc520c9016343'
CALLBACK_URL = 'http://jolinhuang.com'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url
r = client.request_access_token("749b72c13b3116efddfdbf8a14327a05")
access_token = r.access_token # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
# TODO: 在此可保存access token
client.set_access_token(access_token, expires_in)
print client.statuses.user_timeline.get()