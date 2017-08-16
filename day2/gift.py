class Gift:
    def calc(self, dimensions):
        result = 0
        for value in dimensions:
            values_split = list(map(int, value.split('x')))
            small_value = min(values_split)
            result = result + (
                ((2 * values_split[0]) +
                 (2 * values_split[1]) +
                 (2 * values_split[2])) + small_value)

        return result
