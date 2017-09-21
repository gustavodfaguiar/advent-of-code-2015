from day1.santa import Santa


input = open('input.txt').read()
print('To what floor do the instructions take Santa?')
print(Santa(input).current_floor)
print('What is the position of the character that causes Santa to first enter the basement?')
print(Santa(input).first_enter_basement)

