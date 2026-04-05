import unittest
from binary_tree_priority_queue import BinaryTreePriorityQueue

class TestBinaryTreePriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = BinaryTreePriorityQueue()

    def test_empty_queue_errors(self):
        with self.assertRaises(IndexError):
            self.pq.pop()
        
        with self.assertRaises(IndexError):
            self.pq.peek()

    def test_insert_and_peek(self):
        self.pq.insert("Low", 1)
        self.pq.insert("High", 10)
        self.pq.insert("Medium", 5)

        value, priority = self.pq.peek()
        self.assertEqual(value, "High")
        self.assertEqual(priority, 10)

    def test_pop_order(self):
        self.pq.insert("A", 1)
        self.pq.insert("B", 10)
        self.pq.insert("C", 5)
        self.pq.insert("D", 15)

        self.assertEqual(self.pq.pop(), ("D", 15))
        self.assertEqual(self.pq.pop(), ("B", 10))
        self.assertEqual(self.pq.pop(), ("C", 5))
        self.assertEqual(self.pq.pop(), ("A", 1))

    def test_equal_priorities(self):
        self.pq.insert("First", 10)
        self.pq.insert("Second", 10)
        self.pq.insert("Third", 10)

        self.assertEqual(self.pq.pop(), ("Third", 10))
        self.assertEqual(self.pq.pop(), ("Second", 10))
        self.assertEqual(self.pq.pop(), ("First", 10))

    def test_view_all(self):
        self.pq.insert("A", 5)
        self.pq.insert("B", 10)
        
        expected_list = [("B", 10), ("A", 5)]
        self.assertEqual(self.pq.view_all(), expected_list)

if __name__ == "__main__":
    unittest.main()