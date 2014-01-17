from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

handler404 = 'coin_info.views.commonView.http404'
handler500 = 'coin_info.views.commonView.http500'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coinfo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$|^index.htm$',"coin_info.views.index.index"),
    url(r'^loginPage.htm$',"coin_info.views.user.loginPage"),
    url(r'^login.htm$',"coin_info.views.user.login"),
    url(r'^subscribeInfo.htm$',"coin_info.views.subscribe.subscribeInfo"),
    url(r'^showSubscribeData.htm$',"coin_info.views.subscribe.showSubscribeData"),
    url(r"^subscribeRssPage.htm$","coin_info.views.subscribe.subscribeRssPage"),
    url(r"^subscribeWeiboPage.htm$","coin_info.views.subscribe.subscribeWeiboPage"),
    url(r'^admin/', include(admin.site.urls)),
)
