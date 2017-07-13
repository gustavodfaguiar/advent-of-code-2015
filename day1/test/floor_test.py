import unittest
from day1.floor import Floor


class FloorTest(unittest.TestCase):
    def test_up_floor(self):
        self.assertEqual(Floor().floor_position('('), 1)

    def test_down_floor(self):
        self.assertEqual(Floor().floor_position(')'), -1)

    def test_up_down_floor(self):
        self.assertEqual(Floor().floor_position(')())())'), -3)

    def test_up_down_floor_input(self):
        self.assertEqual(Floor().floor_position_input('./fixtures/input.txt'),
                         138)


if __name__ == '__main__':
    unittest.main()
