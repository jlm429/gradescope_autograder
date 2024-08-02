import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from example_submit import MyClass

class TestHomeworkHidden1(unittest.TestCase):
    def setUp(self):
        self.agent = MyClass()

    @weight(50)
    def test_reward_max(self):
        """Evaluate"""
        result = self.agent.solve()
        self.assertGreaterEqual(result, 8)
