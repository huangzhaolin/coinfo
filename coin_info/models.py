from django.db import models
from django.contrib.auth.models import User

class RSSSubscribe(models.Model):
    user=models.ForeignKey(User)
    rssURL=models.CharField("RSS URL XML",max_length=1000)
    rssName=models.CharField("RSS NAME",max_length=100)

    def __str__(self):
        return "%s %s"%(self.rssURL,self.rssName)

class WeiboUserSubscribe(models.Model):
    user=models.ForeignKey(User)
    subscribeUser=models.CharField("SUBSCRIBE USERS",max_length=1000)
    weiboType=models.CharField("WEIBO TYPE",max_length=10,choices=(("SW","SINA WEIBO"),("TW","TWITTER")))

    def __str__(self):
        return "%s %s"%(self.subscribeUser,self.weiboType)