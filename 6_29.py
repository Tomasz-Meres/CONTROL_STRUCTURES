###
# A program that finds N leading prime numbers. The value of N is
# read from the keyboard
#

n = int(input('Enter number: '))
prime_numbers = []
number = 2

#  loop to find prime numbers
while len(prime_numbers) < n:
    divider = 2
    is_prime = True

    # If we don't find a divisor for half of the number,
    # then number is prime
    while divider*divider <= number:
        if number % divider == 0:
            is_prime = False
            break
        divider += 1  # increase the divider

    #  adding number to table with prime numbers if the number is prime
    if is_prime:
        prime_numbers.append(number)

    number += 1  # increase the number

#  display results
print('Prime numbers: ', end=' ')
for i in range(0, len(prime_numbers)):
    print(f'{prime_numbers[i]}', end=' ')
