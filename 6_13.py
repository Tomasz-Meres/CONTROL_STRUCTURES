###
# A program that prints a message when the specified car speed,
# read from the keyboard, has been exceeded.
#

speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if speed_limit_min > speed or speed > speed_limit_max:
    print('Warning: invalid car speed!')
