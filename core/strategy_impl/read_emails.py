from .base_strategy import BaseStrategy
from core.strategy_impl.email_reader import EmailReader
from utils.say import say

class ReadEmails(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        return "I'm supposed to read you your emails"

    def perform(self):
        email_reader = EmailReader()
        email_reader.read_mails()

    def react(self):
        say("reading today's unread emails")
