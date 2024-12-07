###
# A program that checks whether a number entered form the keyboard
# is positive, negative or zero
#

number = int(input('Enter a number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print(f'Number is 0')
