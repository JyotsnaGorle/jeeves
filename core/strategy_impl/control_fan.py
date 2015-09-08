from .base_strategy import BaseStrategy
from utils.connect_to_hw_server import connect_to_hw_server


class ControlFan(BaseStrategy):
    def __init__(self, mode):
        self.type = "h/w"
        self.mode = mode

    def describe(self):
        pass

    def perform(self):
        connect_to_hw_server('%s:fan' % self.mode)
        return

    def react(self):
        pass
