from lab1 import monotony_check

import unittest

class TestMonotonyCheck(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(monotony_check([1, 2, 3]))

    def test_decreasing(self):
        self.assertTrue(monotony_check([3, 2, 1]))

    def test_mixed(self):
        self.assertFalse(monotony_check([1, 5, 2]))

    def test_empty(self):
        self.assertTrue(monotony_check([]))

    def test_single(self):
        self.assertTrue(monotony_check([10]))

    def test_equal(self):
        self.assertTrue(monotony_check([5, 5, 5]))
        
if __name__ == '__main__':
    unittest.main()