import unittest

class Floor:
	def __init__(self):
		self.position = 0


	def floor_position(self, value):
		count = 0
		while count < len(value):
			
			if value[count] == '(':
				self.position += 1
			elif value[count] == ')':
				self.position -= 1

			count += 1

		return self.position



class FloorTest(unittest.TestCase):
	def setUp(self):
		self.floor = Floor()

	def test_up_floor(self):
		self.assertEqual(self.floor.floor_position('('), 1)

	def test_up_floor_2(self):
		self.assertEqual(self.floor.floor_position('(('), 2)

	def test_up_floor_4(self):
		self.assertEqual(self.floor.floor_position('(((('), 4)

	def test_down_floor(self):
		self.assertEqual(self.floor.floor_position(')'), -1)

	def test_down_floor_2(self):
		self.assertEqual(self.floor.floor_position('))'), -2)

	def test_down_floor_4(self):
		self.assertEqual(self.floor.floor_position('))))'), -4)

	def test_up_down_floor(self):
		self.assertEqual(self.floor.floor_position('()'), 0)

	def test_up_down_floor_2(self):
		self.assertEqual(self.floor.floor_position('))((((('), 3)

	def test_up_down_floor_3(self):
		self.assertEqual(self.floor.floor_position(')())())'), -3)


if __name__ == '__main__':
	unittest.main()
