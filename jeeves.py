from __future__ import print_function
from grammifier.grammifier import Grammifier
from strategist.strategist import Strategist
from core.strategies import strategies

while True:
    sentence = raw_input("Type something: ")
    grammifier = Grammifier(sentence)

    mental_state = grammifier.get_stemmed_mental_state()
    action_type = grammifier.get_action_type()

    strategist = Strategist(strategies)
    print(strategist.get_strategy_for(mental_state, action_type))
