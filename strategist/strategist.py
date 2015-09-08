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
                    print("[%d] %s" % (count + 1, strategy.describe()))
                    if strategy.describe():
                        say(strategy.describe())
                    count += 1

                    plans[str(count)] = strategy

                index = user_input("reply: ")
                strategy = plans[index]
            else:
                strategy = strategies[0]

            strategy.react()
            strategy.perform()
        except KeyError:
            print("I don't know what do. Yet, hum nahi phate na Behenchod!")
