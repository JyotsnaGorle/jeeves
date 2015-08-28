from __future__ import print_function
from grammifier.grammifier import Grammifier
from strategist.strategist import Strategist
from core.strategies import strategies

import sys

if len(sys.argv) == 3:
    host = sys.argv[0]
    port = int(sys.argv[1])

while True:
    sentence = raw_input("Type something: ")
    grammifier = Grammifier(sentence)

    print("Referrer is ", grammifier.get_referrer())
    mental_state = grammifier.get_stemmed_mental_state()
    action_type = grammifier.get_action_type()

    strategist = Strategist(strategies)
    strategist.get_strategy_for(mental_state, action_type)
