from day1.floor import Floor


input = open('input.txt').read()
print('To what floor do the instructions take Santa?')
print(Floor(input, 0).santa_current_floor)
print('What is the position of the character that causes Santa to first enter the basement?')
print(Floor(input, -1).santa_current_floor)

