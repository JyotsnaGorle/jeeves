from utils.say import say
from utils.user_input import user_input


class Strategist:
    def __init__(self, strategies):
        self.strategies = strategies

    def get_strategy_for(self, stemmed_mental_state, action_type):
        try:
            strategies = self.strategies[stemmed_mental_state][action_type]

            if len(strategies) > 1:
                say("Okay, what would you like to do?")
                count = 0
                plans = {}

                for strategy in strategies:
                    if strategy.describe():
                        say(strategy.describe())

                    plans[str(count)] = strategy

                reply = user_input("reply:")
                if not reply:
                    return

                action = reply.split(' ')
                strategy = self.strategies[action[0]][action[1]][0]
            else:
                strategy = strategies[0]

            strategy.react()
            strategy.perform()
        except KeyError:
            print("I don't know what do. Yet, hume nahi pata hai!")
