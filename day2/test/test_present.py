from unittest import TestCase, main
from day2.present import Present


class Test_present(TestCase):
	def setUp(self):
		self.present = Present()

	def test_present(self):
		self.assertEqual(self.present.calc(['20x3x11']), 71)


if __name__ == '__main__':
	main()
