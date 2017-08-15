from day2.present import Present


input = open("input.txt").readlines()
dimensions = []

for dimension in input:
    dimension = dimension.strip()
    dimensions.append(dimension)

print('How many total square feet of wrapping paper should they order?')
print(Present().calc(dimensions))
