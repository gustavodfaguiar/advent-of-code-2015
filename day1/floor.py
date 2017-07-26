class Floor:
    MOVE_UP = '('
    MOVE_DOWN = ')'

    def __init__(self, input):
        self.input = input

    def santa_current_floor(self):
        moves_up = self.input.count(self.MOVE_UP)
        moves_down = self.input.count(self.MOVE_DOWN)
        return int(moves_up - moves_down)
