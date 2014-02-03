__author__ = 'zhaolinhuang'
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from coin_info.models import RSSSubscribe
from coin_info.models import WeiboUserSubscribe
from coin_info.log import log
from coin_info.data_collector.rssAPI import RSS
from coin_info.data_collector import sinaWeiboAPI as sina
from weibo import APIError
import json
import traceback
import commonView



@login_required()
def subscribeRssPage(request):
    rsses = RSSSubscribe.objects.filter(user=get_user(request).pk)
    return render(request, "subscribe-rss.html", {"rsses": rsses})


@login_required()
def subscribeWeiboPage(request):
    print sina.weiboSession
    return render(request, "subscribe-weibo.html", {"weiboSession": sina.weiboSession})


@login_required()
def subscribeInfo(request):
    try:
        subscribeParam = request.POST
        subscribeType = subscribeParam.get("type", None)
        if subscribeType == "rss":
            rssSubscribe = RSSSubscribe(user=get_user(request), rssURL=subscribeParam.get("rssURL", None),
                                        rssName=subscribeParam.get("rssName", None))
            rssSubscribe.save()
            return HttpResponseRedirect("subscribeRssPage.htm")
        elif subscribeType == "weibo-user":
            weiboType = subscribeParam.get("weiboType", None)
            if weiboType == "sina":
                weiboUserSubscribe = WeiboUserSubscribe(user=get_user(request),
                                                        subscribeUser=subscribeParam.get("subscribeUser", None),
                                                        weiboType="sina")
                try:
                    weiboUserSubscribe.save()
                except Exception, e:
                    if e.args[0] == 1062:
                        #1 mean susbcribed!
                        HttpResponse(json.dumps(commonView.reponseOK(1), ensure_ascii=False))
                return HttpResponse(json.dumps(commonView.reponseOK(), ensure_ascii=False))

    except Exception, e:
        log.error("subscribe error:%s", e)
        return HttpResponse(status=500)


@login_required()
def showSubscribeData(request):
    try:
        subscribeParam = request.POST
        if subscribeParam.get("type", None) == "rss":
            rss = RSSSubscribe.objects.get(user=get_user(request), rssName=subscribeParam.get("rssName"))
            rssDatas = RSS(rss.rssURL).entites()
            return HttpResponse(json.dumps(rssDatas))
        if subscribeParam.get("type",None)=="weibo":
            weiboSubscribes=WeiboUserSubscribe.objects.filter(user=get_user(request),weiboType="sina")
            weiboTimeLines=[]
            for i in range(0,len(weiboSubscribes)/20+1):
                sinaWeiboUserIDs=map(lambda weiboUser:weiboUser.subscribeUser,weiboSubscribes[i*20:(i+1)*20-1])
                print sinaWeiboUserIDs
                weiboTimeLines.extend(sina.searchWeiboTimeLine(",".join(sinaWeiboUserIDs)))
            return HttpResponse(json.dumps(weiboTimeLines, ensure_ascii=False))
    except Exception, e:
        log.error("subscribe error:%s", traceback.format_exc())
        return HttpResponse(json.dumps(commonView.responseCommonException(e), ensure_ascii=False))


@login_required()
def createSinaWeiboSession(request):
    try:
        sessionCode = request.GET.get("code")
        if sessionCode:
            sina.setAccessToken(sessionCode)
            return HttpResponse(status=200)
        else:
            url = sina.getCodeUrl()
            return HttpResponseRedirect(url)
    except Exception, e:
        log.error("subscribe error:%s", e)
        return HttpResponse(status=500)


@login_required()
def searchSinaWeiboUsers(request):
    try:
        params = request.POST
        uid = params.get("uid")
        screenName = params.get("screenName")
        print screenName
        searchUser = sina.searchUsers(uid, screenName)
        userID = searchUser["id"]
        try:
            WeiboUserSubscribe.objects.get(user=get_user(request),
                                                  subscribeUser=userID,
                                                  weiboType="sina")
        except ObjectDoesNotExist:
            searchUser["subscribed"] = False
        else:
            searchUser["subscribed"] = True
        return HttpResponse(json.dumps(searchUser, ensure_ascii=False))
    except APIError, apiError:
        #1 mean not find!
        if apiError.error_code == 20003:
            return HttpResponse(json.dumps(commonView.reponseOK(1)))
        else:
            return HttpResponse(json.dumps(commonView.responseCommonException(apiError)))

    except Exception, e:
        log.error("subscribe error:%s", e)
        return HttpResponse(json.dumps(commonView.responseCommonException(e)))