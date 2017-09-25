class Gift:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculation_of_wrapping_paper(self):
        total = 0

        for dimension in self.dimensions:
            try:
                length, width, height = list(map(int, dimension.split('x')))
            except Exception:
                raise Exception('Missing parameters')
 
            first = length * width
            second = width * height
            third = height * length

            slack = min([first, second, third])
            paper = sum([first, second, third]) * 2

            total += paper + slack

        return total

    def calculation_of_feet_ribbon(self):
        total = 0

        for dimension in self.dimensions:
            length, width, height = list(map(int, dimension.split('x')))
            min_value = min([length + width, width + height, height + length]) * 2
            total += min_value + width * height * length

        return total
