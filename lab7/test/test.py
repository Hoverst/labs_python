import unittest
import os
from src.main import calculate_minimum_cable


class TestIoTTelecom(unittest.TestCase):
    def setUp(self):
        self.file_normal = "test_normal.csv"
        with open(self.file_normal, "w", encoding="utf-8") as f:
            f.write("K1, K2, 10\n")
            f.write("K1, K3, 15\n")
            f.write("K1, K4, 20\n")
            f.write("K2, K3, 50\n")

        self.file_disconnected = "test_disconnected.csv"
        with open(self.file_disconnected, "w", encoding="utf-8") as f:
            f.write("K1, K2, 100\n")
            f.write("K3, K4, 150\n")

        self.file_empty = "test_empty.csv"
        with open(self.file_empty, "w", encoding="utf-8") as f:
            pass

    def tearDown(self):
        for filename in [self.file_normal, self.file_disconnected, self.file_empty]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_calculate_minimum_cable_normal(self):
        result = calculate_minimum_cable(self.file_normal)
        self.assertEqual(result, (45, 20))

    def test_calculate_minimum_cable_disconnected(self):
        result = calculate_minimum_cable(self.file_disconnected)
        self.assertEqual(result, -1)

    def test_calculate_minimum_cable_empty(self):
        result = calculate_minimum_cable(self.file_empty)
        self.assertEqual(result, (0, 0))

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            calculate_minimum_cable("non_existent_file.csv")


if __name__ == "__main__":
    unittest.main()
