class Strategist:
    def __init__(self, strategies):
        self.strategies = strategies

    def get_strategy_for(self, stemmed_mental_state, action_type):
        try:
            for strategy in self.strategies[stemmed_mental_state][action_type]:
                strategy.react()
                strategy.perform()
        except KeyError:
            print("I don't know what do. Yet, hum nahi phate na Behenchod!")
