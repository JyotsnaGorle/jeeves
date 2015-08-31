from __future__ import print_function
from segregator.segregator import Segregator

import sys

if len(sys.argv) == 3:
    host = sys.argv[1]
    port = int(sys.argv[2])


while True:
    sentence = raw_input("Type something: ")
    segregator = Segregator(sentence)
    segregator.segregate_and_react()
