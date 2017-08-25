from day2.gift import Gift


dimensions = open("input.txt").readlines()
print('How many total square feet of wrapping paper should they order?')
print(Gift().calculation_of_wrapping_paper(dimensions))
print('How many total feet of ribbon should they order?')
print(Gift().calculation_of_feet_ribbon(dimensions))
