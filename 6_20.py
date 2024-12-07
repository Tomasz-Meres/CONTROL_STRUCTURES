###
# A program that converts a decimal number into a binary number.
#

decimal_number = int(input('Enter decimal number: '))
binary = ''  # reversed binary
while decimal_number > 0:
    remainder = decimal_number % 2  # get the reminder
    binary = str(remainder) + binary  # add remainder to the binary string
    decimal_number = decimal_number // 2

print(f'{decimal_number}(10) = {binary}(2)')
