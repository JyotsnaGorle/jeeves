class Strategist:
    def __init__(self, strategies):
        self.strategies = strategies

    def get_strategy_for(self, stemmed_mental_state, action_type):
        for strategy in self.strategies[stemmed_mental_state][action_type]:
            print strategy.describe()
