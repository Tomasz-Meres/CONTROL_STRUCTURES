###
# Sums numbers entered by user and calculates the arithmetic mean of the numbers
#

total_sum = 0
counter = 0

while True:
    number = int(input('Enter a number (0 to stop): '))
    counter += 1
    if number == 0:
        break
    total_sum += number

arithmetic_mean = total_sum / counter

print(f'The total sum of the numbers is: {total_sum}')
print(f'The arithmetic mean of the numbers is {arithmetic_mean}')
