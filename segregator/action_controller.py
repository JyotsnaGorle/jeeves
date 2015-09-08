import nltk

actions = ['turn', 'switch']


class ActionController:
    def __init__(self, sentence):
        self.pos_tags = nltk.pos_tag(sentence)

    def check_if_action(self):
        action_command = self.get_action_command()
        if action_command in actions:
            return True
        return False

    def get_action_command(self):
        for tag in self.pos_tags:
            if str(tag[1]) == 'NN':
                return str(tag[0])

    def get_mode(self):
        for tag in self.pos_tags:
            if str(tag[1]) in ['IN', 'RP']:
                return str(tag[0])

    def get_device(self):
        noun_found = False

        for tag in self.pos_tags:
            if str(tag[1]) == 'NN':
                if not noun_found:
                    noun_found = True
                else:
                    return str(tag[0])
