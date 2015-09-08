from .base_strategy import BaseStrategy
from core.strategy_impl.read_news_and_weather import ReadNewsAndWeather
from datetime import datetime
from utils.connect_to_hw_server import connect_to_hw_server
from utils.say import say

class MakeCoffee(BaseStrategy):
    def __init__(self, mode):
        self.type = "h/w"
        self.mode = mode

    def describe(self):
        return "I am designed to make coffee and coffee only"

    def perform(self):
        connect_to_hw_server('on:coffee')
        return

    def react(self):
        time_of_day = datetime.now().hour

        if time_of_day < 12:
            say("sure, while I make coffee let me update you with today's news and weather")
            news_reader = ReadNewsAndWeather()
            news_reader.read_news()
        else:
            say("sure, give me some time")
