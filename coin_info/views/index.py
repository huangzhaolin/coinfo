__author__ = 'zhaolinhuang'
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from coin_info.models import RSSSubscribe
from django.contrib.auth import get_user

@login_required()
def index(request):
    userObjects=RSSSubscribe.objects.filter(user=get_user(request))
    return render(request, 'index.html',{"rsses":userObjects,"rssStrings":",".join([rss.rssName for rss in userObjects]),"weibo":[]})