class Gift:
    def calculation_of_wrapping_paper(self, dimensions):
        total = 0
        dimensions_new = [ value.strip() for value in dimensions ]

        for dimension in dimensions_new:
            result = []
            length, width, height = list(map(int, dimension.split('x')))

            result.append(length * width)
            result.append(width * height)
            result.append(height * length)
            result_min = min(result)

            mult_result = lambda result: [value * 2 for value in result]
            result = mult_result(result)
            total += sum(result) + result_min

        return total

    def calculation_of_feet_ribbon(self, dimensions):
        total = 0
        dimensions_new = [ value.strip() for value in dimensions ]

        for dimension in dimensions_new:
            result = []
            length, width, height = list(map(int, dimension.split('x')))

            result.append(length)
            result.append(width)
            result.append(height)
            result_sort = sorted(result)

            result_sum = result_sort[0] * 2 + result_sort[1] * 2
            result_mul = result[0] * result[1] * result[2]
            total += result_mul + result_sum

        return total

