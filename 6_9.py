###
# Program that checks whether entered name is a female name
# If name ends with the letter 'a' it is a female names
#

name = input('Enter name: ')

if name[-1] == 'a':
    print(f'{name} -- Polish female name')
