from grammifier.grammifier import Grammifier
import unittest, mock

class GrammifierTestCase(unittest.TestCase):
    def tearDown(self):
        del self.grammifier

    def test_should_get_self_from_sentence_when_1st_person_ref(self):
        self.grammifier = Grammifier("I am feeling hungry")
        self.assertEquals(self.grammifier.getReferrer(), "self")

    def test_should_get_test_from_sentence_when_3rd_person_ref(self):
        self.grammifier = Grammifier("He is feeling hungry")

        with mock.patch('__builtin__.raw_input', return_value = 'test'):
            self.assertEquals(self.grammifier.getReferrer(), "test")

    def test_should_return_stem_of_verb_of_mental_state(self):
        self.grammifier = Grammifier("I need shitty")
        self.assertEquals(self.grammifier.getStemmedMentalState(), "need")

    def test_should_return_type_of_action(self):
        self.grammifier = Grammifier("I am feeling like crap")
        self.assertEquals(self.grammifier.get_action_type(), "crap")

if __name__ == '__main__':
    unittest.main()
