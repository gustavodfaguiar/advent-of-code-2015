class Floor:
    @staticmethod
    def calc_position(value):
        up = value.count('(')
        down = value.count(')')
        return up - down

    def floor_position_input(self, floors):
        value = open(floors).read()
        return self.calc_position(value)
