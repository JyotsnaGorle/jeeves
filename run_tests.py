from grammifier.grammifier import Grammifier
from strategist.strategist import Strategist
import unittest, mock

class GrammifierTestCase(unittest.TestCase):
    def tearDown(self):
        del self.grammifier

    def test_should_get_self_from_sentence_when_1st_person_ref(self):
        self.grammifier = Grammifier("I am feeling hungry")
        self.assertEquals(self.grammifier.get_referrer(), "self")

    def test_should_get_test_from_sentence_when_3rd_person_ref(self):
        self.grammifier = Grammifier("He is feeling hungry")

        with mock.patch('__builtin__.raw_input', return_value = 'test'):
            self.assertEquals(self.grammifier.get_referrer(), "test")

    def test_should_return_stem_of_verb_of_mental_state(self):
        self.grammifier = Grammifier("I need coffee")
        self.assertEquals(self.grammifier.get_stemmed_mental_state(), "need")

    def test_should_return_stem_of_verb_of_mental_state(self):
        self.grammifier = Grammifier("I am feeling lonely")
        self.assertEquals(self.grammifier.get_stemmed_mental_state(), "feel")

    def test_should_return_stem_of_verb_of_mental_state(self):
        self.grammifier = Grammifier("I am bored")
        self.assertEquals(self.grammifier.get_stemmed_mental_state(), "bore")

    def test_should_return_type_of_action(self):
        self.grammifier = Grammifier("I am feeling like crap")
        self.assertEquals(self.grammifier.get_action_type(), "crap")

class BaseStrategy:
    def describe(self):
        pass

    def perform(self):
        pass

class PlayMusic(BaseStrategy): pass
class StartTV(BaseStrategy): pass
class OpenFacebook(BaseStrategy): pass

strategies = {
    "feel": {
        "bored": [PlayMusic(), StartTV()],
        "lonely": [OpenFacebook()]
    },
    "need": {
        "music": [PlayMusic()]
    }
}

class StrategistTestCase(unittest.TestCase):
    def setUp(self):
        self.strategist = Strategist(strategies)

    def tearDown(self):
        del self.strategist

    def test_should_return_list_of_strategies(self):
        expected_list = self.strategist.get_strategy_for("feel", "bored")

        self.assertTrue(isinstance(expected_list[0], PlayMusic))
        self.assertTrue(isinstance(expected_list[1], StartTV))

if __name__ == '__main__':
    unittest.main()

