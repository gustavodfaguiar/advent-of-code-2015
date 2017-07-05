from unittest import TestCase, main

class Present:
	def calc(self, values):
		values_split = list(map(int, values.split('x')))
		small_value = min(values_split)
		result = ((2 * values_split[0]) + (2 * values_split[1]) + (2 * values_split[2])) + small_value
		return result


class Test_present(TestCase):
	def setUp(self):
		self.present = Present()

	def test_present(self):
		self.assertEqual(self.present.calc('20x3x11'), 71)


if __name__ == '__main__':
	main()