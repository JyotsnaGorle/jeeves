from __future__ import print_function
from segregator.segregator import Segregator
from julius_connector.julius_connector import connect_to_julius

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(description="P.G. Wodehouse couldn't have imagined me better.")
parser.add_argument("--input", help="specify the input source mic/stdin, default is stdin")
parser.add_argument("--host", help="specify julius' host, default is localhost")
parser.add_argument("--port", help="specify julius' port, default is 10500", type=int)
args = parser.parse_args()

process = subprocess.Popen([sys.executable, "chat_ui/chat_ui_server.py"])

if args.input and args.input == "mic":
    connect_to_julius(args.host or "localhost", args.port or 10500)
else:
    while True:
        sentence = raw_input("Type something: ")
        segregator = Segregator(sentence)
        segregator.segregate_and_react()
