from __future__ import print_function
from grammifier.grammifier import Grammifier
from strategist.strategist import Strategist
from core.strategies import Strategies

sentences = ["I am feeling hungry", "He is feeling bored", "I need music"]

for sentence in sentences:
    grammifier = Grammifier(sentence)

    mental_state = grammifier.getStemmedMentalState()
    action_type = grammifier.get_action_type()

    strategist = Strategist(Strategies().get_strategies())
    print(strategist.get_strategy_for(mental_state, action_type))
