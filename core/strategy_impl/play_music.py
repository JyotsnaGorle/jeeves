from .base_strategy import BaseStrategy

class PlayMusic(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        return "I'm supposed to Play Music"

    def perform(self):
        return "Playing music..."

    def react(self):
        pass
