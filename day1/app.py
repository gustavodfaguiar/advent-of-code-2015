from day1.floor import Floor


input = open('input.txt').read()
santa_current = Floor(input).santa_current_floor()

print('To what floor do the instructions take Santa?')
print(santa_current)
