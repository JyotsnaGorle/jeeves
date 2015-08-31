from __future__ import print_function
from segregator.segregator import Segregator

import argparse

parser = argparse.ArgumentParser(description="P.G. Wodehouse couldn't have imagined me better.")
parser.add_argument("--input", help="specify the input source mic/stdin, default is stdin")
parser.add_argument("--host", help="specify julius' host, default is localhost")
parser.add_argument("--port", help="specify julius' port, default is 10500", type=int)
args = parser.parse_args()

if args.input and args.input == "mic":
    host = args.host or "localhost"
    port = args.port or 10500
    print("Jeeves is preparing to listen at %s:%d..." % (host, port))

while True:
    sentence = raw_input("Type something: ")
    segregator = Segregator(sentence)
    segregator.segregate_and_react()
