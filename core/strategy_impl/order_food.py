from .base_strategy import BaseStrategy
from subprocess import call
import webbrowser

class OrderFood(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        pass

    def perform(self):
        url = "http://www.zomato.com"
        webbrowser.open(url,new=2)

    def react(self):
        call(["say", "unfortunately I cannot feed you, but I can help you find some food"])

