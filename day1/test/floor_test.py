import unittest
from day1.floor import Floor


class FloorTest(unittest.TestCase):
    def test_up_floor(self):
        self.assertEqual(Floor('(').santa_current_floor(), 1)

    def test_down_floor(self):
        self.assertEqual(Floor(')').santa_current_floor(), -1)

    def test_up_down_floor(self):
        self.assertEqual(Floor(')())())').santa_current_floor(), -3)


if __name__ == '__main__':
    unittest.main()
