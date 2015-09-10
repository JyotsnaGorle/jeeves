from __future__ import print_function
from .base_strategy import BaseStrategy
from conf.data_sources import data_sources
from utils.say import say
from utils.user_input import user_input

import feedparser
import re


class ReadNewsAndWeather(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        return "Listen to the news and weather"

    def perform(self):
        self.read_news()
        self.tell_weather()

    def react(self):
        say("Fetching today's news and weather for you...")

    def read_news(self):
        sources = data_sources['news_urls']

        say("I can read news from...")
        for source in sources.keys():
            say(source)
        say("please tell me where would you like to hear it from?")
        feed = feedparser.parse(sources[user_input()])

        say("So, the top 3 stories are...")
        for entry in feed.entries[:count]:
            news_to_read = entry["description"]
            say(re.sub('<[^<]+?>', '', news_to_read.split('.')[0]))

    def tell_weather(self):
        pass
