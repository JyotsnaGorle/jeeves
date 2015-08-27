from __future__ import print_function
import nltk, numpy

stemmer = nltk.stem.porter.PorterStemmer()

class Grammifier:
    def __init__(self, sentence):
        self.pos_tags = nltk.pos_tag(nltk.word_tokenize(sentence))
        self.parse_index = 0

    def stem(self, word):
        return str(stemmer.stem_word(word))

    def get_referrer(self):
        for tag in self.pos_tags:
            if str(tag[1]) == 'VBZ':
                return raw_input("Who is %s?: " % self.pos_tags[self.parse_index - 1][0])
            elif str(tag[1]) == 'VBP':
                return "self"

            self.parse_index += 1

    def get_stemmed_mental_state(self):
        matches = ['VBN', 'VBP', 'VBG']

        for index in range(self.parse_index, len(self.pos_tags)):
            if str(self.pos_tags[index][1]) in ['VBP', 'VBZ']:
                next = self.pos_tags[index + 1]
                state = None

                if str(next[1]) == 'VBG':
                    state = self.stem(str(next[0]))
                elif str(next[1]) in ['JJ','RB']:
                    state = self.stem(str(next[0]))
                elif str(next[1]) == 'VBN':
                    state = 'feel'
                else:
                    state = self.stem(str(self.pos_tags[index][0]))

                return state

    def get_action_type(self):
        actions = ['NN', 'JJ', 'VBN','RB']

        for tag in self.pos_tags:
            if str(tag[1]) in actions:
                return str(tag[0])
