from __future__ import print_function
from .base_strategy import BaseStrategy
from conf.data_sources import data_sources
from utils.say import say

import feedparser

class ReadNewsAndWeather(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        pass

    def perform(self):
        self.read_news()
        self.tell_weather()

    def react(self):
        say("Fetching today's news and weather for you...")

    def read_news(self):
        rss_read = feedparser.parse(data_sources['news_url'])
        entries = rss_read.entries

        for entry in entries:
            news_to_read = entry["description"].split(".")[0].strip()
            print(news_to_read)

    def tell_weather(self):
        pass
