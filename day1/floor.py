class Floor:
    @staticmethod
    def calc_position(self, value):
        time_up = 0
        time_down = 0
        count = 0
        while count < len(value):
            if value[count] == '(':
                time_up += 1
            elif value[count] == ')':
                time_down += 1

        count += 1

        return time_up - time_down

    def floor_position(self, floors):
        value = floors
        return self.calc_position(self, value)

    def floor_position_input(self, floors):
        value = open(floors).read()
        return self.calc_position(self, value)
