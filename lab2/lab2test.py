import unittest
from lab2 import find_min_square_size

class TestMinSquareSize(unittest.TestCase):

    def test_original_case(self):
        self.assertEqual(find_min_square_size(40, 63, 22), 252)

    def test_single_item(self):
        self.assertEqual(find_min_square_size(2, 3, 1), 3)

    def test_square_items(self):
        self.assertEqual(find_min_square_size(2, 2, 4), 4)

    def test_tall_rectangles(self):
        self.assertEqual(find_min_square_size(1000000000,  999999999, 2),  1999999998 )

if __name__ == '__main__':
    unittest.main()