from __future__ import print_function
from .base_strategy import BaseStrategy
from conf.data_sources import data_sources
from utils.say import say

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
        indexed_source = []

        sources = data_sources['news_urls']

        say("I can read news from...")
        for source in sources.keys():
            say(source)
            indexed_source.append(sources[source])

        say("And, very soon i will be able to hear you. For now please type the choice from 1 to %d" % len(sources))
        choice = int(raw_input("choice[1-%d]: " % len(sources)))
        say("And, how many headlines would you like to hear?")
        count = int(raw_input("how many: "))

        feed = feedparser.parse(indexed_source[choice - 1])

        say("So, the top stories are...")
        for entry in feed.entries:
            news_to_read = entry["description"]
            say(re.sub('<[^<]+?>', '', news_to_read.split('.')[0]))
            count -= 1
            if count == 0:
                break

    def tell_weather(self):
        pass
