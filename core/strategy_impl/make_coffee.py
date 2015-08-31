from time import strftime
from .base_strategy import BaseStrategy
from core.strategy_impl.read_news_and_weather import ReadNewsAndWeather
from utils.say import say


class MakeCoffee(BaseStrategy):
    def __init__(self):
        self.type = "h/w"

    def describe(self):
        return "I am designed to make coffee and coffee only"

    def perform(self):
        pass

    def react(self):
        time_of_day = int(strftime("%H"))
        if time_of_day < 12:
            say("sure, while I make coffee let me update you with today's news and weather")
            newsReader = ReadNewsAndWeather()
            newsReader.read_news()

        else:
            say("sure, give me some time")
