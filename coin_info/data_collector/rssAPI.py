__author__ = 'zhaolinhuang'
import feedparser
import time
class RSS(object):
    def __init__(self,url):
        self.url=url
        self.data=feedparser.parse(url)
    def entites(self):
        formatEntites=[]
        for entry in self.data["entries"]:
            formatEntites.append({
                "title":entry["title_detail"]["value"],
                "url":entry["id"],
                "value":entry["summary_detail"]["value"],
                "tags":entry["tags"],
                "time":time.strftime("%Y-%m-%d %H:%M:%S",entry["published_parsed"])
            })
        return formatEntites
