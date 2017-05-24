import random
import unittest

class RandomTest(unittest.TestCase):
    """Test case used to test the function of the "random" module."""

    def test_choice(self):
        my_list = list(range(10))
        elt = random.choice(my_list)
        self.assertIn(elt, my_list)

