from .base_strategy import BaseStrategy
import webbrowser

class OpenFacebook(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        pass

    def perform(self):
        url = "http://www.facebook.com"
        webbrowser.open(url,new=2)
