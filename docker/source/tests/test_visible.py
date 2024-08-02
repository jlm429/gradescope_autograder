import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from example_submit import MyClass

class TestHomeworkVisible1(unittest.TestCase):
    def setUp(self):
        print("setting up")

    @weight(25)
    def test_evaluate(self):
        """Evaluate"""
        self.assertGreaterEqual(42, 42)


class TestHomeworkVisible2(unittest.TestCase):
    def setUp(self):
        self.agent = MyClass()

    @weight(25)
    def test_reward_max(self):
        """Evaluate"""
        result = self.agent.solve()
        self.assertGreaterEqual(result, 8)
