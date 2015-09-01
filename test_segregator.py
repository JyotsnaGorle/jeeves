from segregator.segregator import Segregator

import unittest

class SegregatorTestCase(unittest.TestCase):
    def tearDown(self):
        del self.segregator

    def test_should_return_true_if_sentence_is_a_greeting(self):
        self.segregator = Segregator("good morning")
        self.assertTrue(self.segregator.check_if_greeting())

    def test_should_return_false_if_sentence_is_not_a_greeting(self):
        self.segregator = Segregator("i am bored")
        self.assertFalse(self.segregator.check_if_greeting())

if __name__ == '__main__':
    unittest.main()
