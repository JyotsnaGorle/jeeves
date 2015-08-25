from __future__ import print_function
import nltk, numpy

class Grammifier:
    def __init__(self, sentence):
        self.pos_tags = nltk.pos_tag(nltk.word_tokenize(sentence))

    def getReferrer(self):
        index = 0

        for tag in self.pos_tags:
            if str(tag[1]) == 'VBZ':
                return raw_input("Who is %s?: " % self.pos_tags[index - 1][0])
            elif str(tag[1]) == 'VBP':
                return "self"

            index += 1

    def getStemmedMentalState(self):
        matches = ['VBN', 'VBP', 'VBG']

        for tag in self.pos_tags:
            if str(tag[1]) in matches:
                return str(tag[0]).replace('ing', '')

    def get_action_type(self):
        actions = ['NN', 'JJ']

        for tag in self.pos_tags:
            if str(tag[1]) in actions:
                return str(tag[0])
