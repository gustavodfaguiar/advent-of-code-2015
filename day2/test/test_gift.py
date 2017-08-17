from unittest import TestCase, main
from day2.gift import Gift


class Test_gift(TestCase):
    def setUp(self):
        self.gift = Gift()

    def test_one_gift(self):
        self.assertEqual(
            self.gift.calculation_of_wrapping_paper(['2x3x4']), 58)

    def test_two_gift(self):
        self.assertEqual(
            self.gift.calculation_of_wrapping_paper(['2x3x4', '1x1x10']), 101)

if __name__ == '__main__':
    main()
