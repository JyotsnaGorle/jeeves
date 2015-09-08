from __future__ import print_function
from .base_strategy import BaseStrategy
from utils.say import say
from utils.user_input import user_input

import os

try:
    import cPickle as pickle
except ImportError:
    import pickle


class MemBlock:
    def __init__(self):
        self.question = ""
        self.guess = ""
        self.no1 = None
        self.no2 = None


def read_memory():
    with open('brains', 'rb') as brains:
        root = pickle.load(brains)

    return root


def write_memory(root):
    with open('brains', 'wb') as brains:
        pickle.dump(root, brains, pickle.HIGHEST_PROTOCOL)


def mem_walker(brains_found):
    flag1, flag2 = False, False

    if not brains_found:
        block = MemBlock()
        block.question = "Is it 4 legged?"
        block.guess = "Dog"

        write_memory(block)
        mem_walker(True)
    else:
        block = read_memory()
        current_block = block

        while True:
            print("[Jeeves] %s" % current_block.question)
            say(current_block.question)
            reply = user_input("reply: ").lower()

            if reply in ["yes", "y"]:
                print("[Jeeves] %s" % current_block.guess)
                say("So, Is it a %s?" % current_block.guess)
                reply = user_input("reply: ").lower()

                if reply in ["yes", "y"]:
                    say("Awesome!! I'm getting good at this!")
                    break
                else:
                    if not current_block.no2:
                        flag2 = True
                        break
                    else:
                        current_block = current_block.no2
            else:
                if not current_block.no1:
                    flag1 = True
                    break
                else:
                    current_block = current_block.no1

        if flag1 or flag2:
            temp = MemBlock()

            say("Okay, I give up!")
            say("I want to learn from you now...")
            say("Type a question related to the animal you thought.")
            say("For example: Does it have stripes? Or does it run fast?")
            temp.question = user_input("reply: ")

            say("Okay, tell me the creature you thought of")
            temp.guess = user_input("reply: ")

            say("Awesome. Assuming what you taught me is correct, I'll definitely remember it!")

            if flag1:
                current_block.no1 = temp
            else:
                current_block.no2 = temp

            write_memory(block)


def check():
    say("Think of an animal and when you're ready hit the enter key.")
    raw_input()

    if not os.path.exists("brains"):
        say("I guess we are playing this game for the first time, so pardon my ignorance.")
        mem_walker(False)
    else:
        mem_walker(True)


class PlayAnimalGame(BaseStrategy):
    def __init__(self):
        self.type = "s/w"

    def describe(self):
        return "Would you play the guess the animal game?"

    def perform(self):
        reply = "yes"

        while reply in ["yes", "y"]:
            check()

            say("Shall we play again?")
            reply = user_input("reply: ").lower()

        say("It was nice playing with you!")

    def react(self):
        say("Okay, Lets play a game...")
