import os


class Floor:
    @staticmethod
    def calc_position(value):
        up = value.count('(')
        down = value.count(')')
        return up - down

    def floor_position(self, floors):
        return self.calc_position(floors)

    def floor_position_input(self, floors):
        script_dir = os.path.dirname(__file__)
        rel_path = "test/fixtures/input.txt"
        value = open(os.path.join(script_dir, rel_path)).read()
        return self.calc_position(value)
