__author__ = 'zhaolinhuang'
from pyquery import PyQuery as pq
from coin_info.models import BTCWallet
from django.db.models import Max
import datetime
import threading
import logging

log = logging.getLogger("coinfo")


def getBTCTOP100DATA(date):
    """
    get btc top 10 data
    """
    htmlData = pq(url="http://btc.ondn.net/history/%s" % date)
    head = htmlData(".content").find("h1").html()
    date = head.replace("History", "").strip()
    trs = htmlData("TR")
    for tr in trs[1:-2]:
        try:
            tds = pq(tr).find("TD")
            rank = int(pq(tds[0]).html())
            address = pq(tds[1]).find("a").html()
            balance = float(pq(tds[2]).html())
            rankDate = date.split("-")
            btcWallet = BTCWallet(rankIndex=rank, address=address, balance=balance,
                                  rankDate=datetime.datetime(year=int(rankDate[0]), month=int(rankDate[1]),
                                                             day=int(rankDate[2])))
            btcWallet.save(force_insert=True)
        except Exception, e:
            print tds
    return trs


def syncData():
    def doSync():
        startDateTime = BTCWallet.objects.all().aggregate(Max('rankDate')).get('rankDate__max')
        while int(historyDate.strftime("%S")) < int(datetime.datetime.now().strftime("%S")):
            log.info("SYNC DATE ON :%s" % startDateTime)
            getBTCTOP100DATA(historyDate.strftime("%Y%m%d"))
            startDateTime = startDateTime + datetime.timedelta(days=1)

    threading.Thread(target=doSync).start()
