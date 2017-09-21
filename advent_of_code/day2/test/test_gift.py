from unittest import TestCase, main
from advent_of_code.day2.gift import Gift


class Test_gift(TestCase):
    def test_one_gift(self):
        self.assertEqual(
            Gift(['2x3x4']).calculation_of_wrapping_paper(), 58)

    def test_two_gift(self):
        self.assertEqual(
            Gift(['2x3x4', '1x1x10']).calculation_of_wrapping_paper(), 101)

    def test_value_with_line_break(self):
        self.assertEqual(
            Gift(['2x3x4\n']).calculation_of_wrapping_paper(), 58)

    def test_value_feet_ribbon(self):
        self.assertEqual(
            Gift(['2x3x4']).calculation_of_feet_ribbon(), 34)

    def test_empty_list(self):
        self.assertEqual(
            Gift([]).calculation_of_wrapping_paper(), 0)

    def test_two_dimensions(self):
        self.assertEqual(
            Gift(['2x2']).calculation_of_wrapping_paper(), 0)

    def test_negative_number(self):
        self.assertEqual(
            Gift(['-2x3x4']).calculation_of_wrapping_paper(), 0)

if __name__ == '__main__':
    main()
