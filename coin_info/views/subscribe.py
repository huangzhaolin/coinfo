__author__ = 'zhaolinhuang'
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from coin_info.models import RSSSubscribe
from coin_info.log import log
from coin_info.data_collector.rssAPI import  RSS
import json
import commonView

@login_required()
def subscribeRssPage(request):
    rsses=RSSSubscribe.objects.filter(user=get_user(request).pk)
    return render(request,"subscribe-rss.html",{"rsses":rsses})

@login_required()
def subscribeWeiboPage(request):
    return render(request,"subscribe-weibo.html")

@login_required()
def subscribeInfo(request):
    try:
        subscribeParam = request.POST
        print subscribeParam
        if subscribeParam.get("type", None) == "rss":
            rssSubscribe = RSSSubscribe(user=get_user(request), rssURL=subscribeParam.get("rssURL", None),
                rssName=subscribeParam.get("rssName", None))
            rssSubscribe.save()
        return HttpResponseRedirect("subscribeRssPage.htm")
    except Exception,e:
        log.error("subscribe error:%s",e)
        return HttpResponse(status=500)

@login_required()
def showSubscribeData(request):
    try:
        subscribeParam=request.POST
        if subscribeParam.get("type", None) == "rss":
            rss=RSSSubscribe.objects.get(user=get_user(request),rssName=subscribeParam.get("rssName"))
            rssDatas=RSS(rss.rssURL).entites()
            return HttpResponse(json.dumps(rssDatas))
    except Exception,e:
        log.error("subscribe error:%s",e)
        return HttpResponse(json.dumps(commonView.responseCommon(e)))

