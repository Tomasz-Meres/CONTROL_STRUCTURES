###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result
#

number1 = int(input('Eneter first number: '))
number2 = int(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    print('Incorrect data')
    result = 0

if result:
    print(f'{number1} {operator} {number2} = {result}')