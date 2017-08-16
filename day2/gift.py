class Gift:
    def calculation_of_wrapping_paper(self, dimensions):
        result = 0
        dimensions_new = []
        for dimension in list(dimensions):
            dimension = dimension.strip()
            dimensions_new.append(dimension)

        for dimension in dimensions_new:
            length, width, height = list(map(int, dimension.split('x')))
            result += (
                ((2 * length * width) +
                 (2 * width * height) +
                 (2 * height * length)))
        return result
