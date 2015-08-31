from utils.say import say

import nltk

stemmer = nltk.stem.porter.PorterStemmer()

class Grammifier:
    def __init__(self, sentence):
        self.pos_tags = nltk.pos_tag(sentence)
        self.parse_index = 0

    def stem(self, word):
        return str(stemmer.stem_word(word))

    def speak(self, what):
        say(what)

    def get_referrer(self):
        for tag in self.pos_tags:
            if str(tag[1]) == 'VBZ':
                self.speak("Who is %s" % self.pos_tags[self.parse_index - 1][0])
                return raw_input("reply: ")
            elif str(tag[1]) == 'VBP':
                return "self"

            self.parse_index += 1

    def get_stemmed_mental_state(self):
        for index in range(self.parse_index, len(self.pos_tags)):
            if str(self.pos_tags[index][1]) in ['VBP', 'VBZ']:
                next = self.pos_tags[index + 1]
                state = None

                if str(next[1]) == 'VBG':
                    state = self.stem(str(next[0]))
                elif str(next[1]) in ['VBN', 'JJ', 'RB']:
                    state = 'feel'
                else:
                    state = self.stem(str(self.pos_tags[index][0]))

                return state

    def get_action_type(self):
        actions = ['NN', 'JJ', 'VBN', 'RB']

        for tag in self.pos_tags:
            if str(tag[1]) in actions:
                return str(tag[0])
