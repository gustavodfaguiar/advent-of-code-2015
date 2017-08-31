class Gift:
    TOTAL = 0

    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculation_of_wrapping_paper(self):
        dimensions_new = self.remove_whitespaces(self.dimensions)

        for dimension in dimensions_new:
            result = []
            length, width, height = list(map(int, dimension.split('x')))

            result.append(length * width)
            result.append(width * height)
            result.append(height * length)
            result_min = min(result)

            mult_result = lambda result: [value * 2 for value in result]
            result = mult_result(result)
            self.TOTAL += sum(result) + result_min

        return self.TOTAL

    def calculation_of_feet_ribbon(self):
        dimensions_new = self.remove_whitespaces(self.dimensions)

        for dimension in dimensions_new:
            result = []
            length, width, height = list(map(int, dimension.split('x')))

            result.append(length)
            result.append(width)
            result.append(height)
            result_sort = sorted(result)

            result_sum = result_sort[0] * 2 + result_sort[1] * 2
            result_mul = result[0] * result[1] * result[2]
            self.TOTAL += result_mul + result_sum

        return self.TOTAL

    def remove_whitespaces(self, dimensions):
        return [ value.strip() for value in dimensions ]
