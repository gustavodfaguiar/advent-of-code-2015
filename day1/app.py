from day1.floor import Floor


input = open('input.txt').read()
print('To what floor do the instructions take Santa?')
print(Floor(input).santa_current_floor)
