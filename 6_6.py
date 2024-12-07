###
# A program that ask for the number of hours parking,
# then calculates and prints the correct fee
#

num_of_hours = int(input('Enter number of hours of parking '))

if 1 <= num_of_hours <= 2:
    print('The fee is 5 PLN')
elif 3 <= num_of_hours <= 6:
    print('The fee is 15 PLN')
elif num_of_hours > 6:
    print('The fee is 20 PLN')
