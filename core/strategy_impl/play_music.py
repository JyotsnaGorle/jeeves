from .base_strategy import BaseStrategy
from utils.say import say

class PlayMusic(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        return "I'm supposed to Play Music"

    def perform(self):
        pass

    def react(self):
        say("Okay, lets play some music...")
