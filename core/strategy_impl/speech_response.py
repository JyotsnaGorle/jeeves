from core.strategy_impl.base_strategy import BaseStrategy
from utils.say import say

responses = {
    "tired": "I suggest you consume a red bull",
    "sleepy": "you should get some sleep"
}

class SpeechResponse(BaseStrategy):

    def __init__(self, action):
        self.type = "s/w"
        self.action = action

    def describe(self):
        pass

    def perform(self):
        global responses

        for response_type in responses.keys():
            if self.action == response_type:
                say(responses[response_type])
                break
        else:
            say("Sorry, I cannot help you with that")

    def react(self):
        pass
