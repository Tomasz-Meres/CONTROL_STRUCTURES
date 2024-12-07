###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#

month = int(input('Enter month number (1,12) '))

if 1 <= month <= 3:
    quarter = 1
elif 4 <= month <= 6:
    quarter = 2
elif 7 <= month <= 9:
    quarter = 3
elif 10 <= month <= 12:
    quarter = 4
else:
    quarter = 0
    print('Incorrect value')

if quarter:
    print(f'Month {month} is in quarter {quarter}')
