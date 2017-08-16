class Gift:
    def calculation_of_wrapping_paper(self, dimensions):
        result = 0
        dimensions_new = []
        for dimension in dimensions:
            dimension = dimension.strip()
            dimensions_new.append(dimension)

        for value in dimensions_new:
            values_split = list(map(int, value.split('x')))
            small_value = min(values_split)
            result = result + (
                ((2 * values_split[0]) +
                 (2 * values_split[1]) +
                 (2 * values_split[2])) + small_value)

        return result
