class Santa:
    MOVE_UP = '('
    MOVE_DOWN = ')'
    BASEMENT = -1

    def __init__(self, input):
        self.input = input

    @property
    def current_floor(self):
        moves_up = self.input.count(self.MOVE_UP)
        moves_down = self.input.count(self.MOVE_DOWN)
        return moves_up - moves_down

    @property
    def first_enter_basement(self):
        floor = 0
        for index, move in enumerate(self.input):
            if move == self.MOVE_UP:
                floor += 1
            else:
                floor -= 1

            if floor == self.BASEMENT:
                return index + 1
