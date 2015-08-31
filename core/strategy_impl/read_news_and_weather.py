from __future__ import print_function
import feedparser

class ReadNewsAndWeather:
    def __init__(self):
        self.type = "s/w"

    def read_news(self):
        rss_read = feedparser.parse(
            "http://dynamic.feedsportal.com/pf/555218/http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms")
        entries = rss_read.entries

        for entry in entries:
            news_to_read = entry["description"].split(".")[0].strip()
            print(news_to_read)

    def tell_weather(self):
        pass
