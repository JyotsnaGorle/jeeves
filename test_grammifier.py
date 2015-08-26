from grammifier.grammifier import Grammifier
import unittest, mock

class GrammifierTestCase(unittest.TestCase):
    def tearDown(self):
        del self.grammifier

    def mock_referrer_call(self):
        with mock.patch('__builtin__.raw_input', return_value = 'test'):
            self.grammifier.get_referrer()

    def test_should_get_self_from_sentence_when_1st_person_ref(self):
        self.grammifier = Grammifier("I am feeling hungry")
        self.assertEquals(self.grammifier.get_referrer(), "self")

    def test_should_get_test_from_sentence_when_3rd_person_ref(self):
        self.grammifier = Grammifier("He is feeling hungry")

        with mock.patch('__builtin__.raw_input', return_value = 'test'):
            self.assertEquals(self.grammifier.get_referrer(), "test")

    def test_should_return_stem_of_verb_of_mental_state_with_no_vbg(self):
        self.grammifier = Grammifier("I need coffee")
        self.assertEquals(self.grammifier.get_stemmed_mental_state(), "need")

    def test_should_return_stem_of_verb_of_mental_state_with_vbg(self):
        self.grammifier = Grammifier("I am feeling lonely")
        self.mock_referrer_call()
        self.assertEquals(self.grammifier.get_stemmed_mental_state(), "feel")

    def test_should_return_stem_of_verb_of_mental_state_with_vbp(self):
        self.grammifier = Grammifier("I am bored")
        self.mock_referrer_call()
        self.assertEquals(self.grammifier.get_stemmed_mental_state(), "feel")

    def test_should_return_type_of_action(self):
        self.grammifier = Grammifier("I am feeling like crap")
        self.mock_referrer_call()
        self.assertEquals(self.grammifier.get_action_type(), "crap")

if __name__ == '__main__':
    unittest.main()
