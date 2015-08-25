from strategist.strategist import Strategist
import unittest

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
