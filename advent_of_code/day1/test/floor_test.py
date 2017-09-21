import unittest
from day1.santa import Santa


class FloorTest(unittest.TestCase):
    def test_up_floor(self):
        self.assertEqual(Santa('(').current_floor, 1)

    def test_down_floor(self):
        self.assertEqual(Santa(')').current_floor, -1)

    def test_up_down_floor(self):
        self.assertEqual(Santa(')())())').current_floor, -3)

    def test_up_down_floor_basement(self):
        self.assertEqual(Santa('()())').first_enter_basement, 5)

if __name__ == '__main__':
    unittest.main()
