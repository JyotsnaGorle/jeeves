from __future__ import print_function
import nltk, numpy

class Grammifier:
    def __init__(self, sentence):
        self.pos_tags = nltk.pos_tag(nltk.word_tokenize(sentence))

    def get_referrer(self):
        index = 0

        for tag in self.pos_tags:
            if str(tag[1]) == 'VBZ':
                return raw_input("Who is %s?: " % self.pos_tags[index - 1][0])
            elif str(tag[1]) == 'VBP':
                return "self"

            index += 1

    def get_stemmed_mental_state(self):
        matches = ['VBN', 'VBP', 'VBG']
        porter_stemmer = nltk.stem.porter.PorterStemmer()
        first_verb_found = False

        for tag in self.pos_tags:
            if str(tag[1]) in ['VBZ', 'VBP'] and not first_verb_found:
                first_verb_found = True
                verb = str(tag[0])
                continue

            if str(tag[1]) in matches and first_verb_found:
                return str(porter_stemmer.stem_word(str(tag[0])))

        if first_verb_found:
            return porter_stemmer.stem_word(verb)

    def get_action_type(self):
        actions = ['NN', 'JJ', 'VBN']

        for tag in self.pos_tags:
            if str(tag[1]) in actions:
                return str(tag[0])
