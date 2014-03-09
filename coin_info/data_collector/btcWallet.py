__author__ = 'zhaolinhuang'
from pyquery import PyQuery as pq
#from coin_info.models import BTCWallet
import datetime


def getBTCTOP100DATA(date):
    """
    get btc top 10 data
    """
    htmlData = pq(url="http://btc.ondn.net/history/%s" % date)
    head = htmlData(".content").find("h1").html()
    date = head.replace("History", "").strip()
    trs = htmlData("TR")
    for tr in trs[:-2]:
        tds = pq(tr).find("TD")
        rank = pq(tds[0]).html()
        address = pq(tds[1]).find("a").html()
        balance = pq(tds[2]).html()
        rankDate = date
        print "%s %s %s %s"%(rank, address, balance, rankDate)
        #BTCWallet(rank=rank, address=address, balance=balance, rankDate=rankDate)
    return trs


def syncData():
    historyDate = datetime.date(year=2014, month=3, day=5)
    while int(historyDate.timetuple()) < int(datetime.datetime.now().strftime("%S")):
        getBTCTOP100DATA(historyDate.strftime("%Y%m%d"))
        historyDate + datetime.timedelta(days=1)


syncData()
