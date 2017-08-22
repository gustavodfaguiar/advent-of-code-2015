class Gift:
    def calculation_of_wrapping_paper(self, dimensions):
        total = 0
        dimensions_new = []
        for dimension in list(dimensions):
            dimension = dimension.strip()
            dimensions_new.append(dimension)

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
