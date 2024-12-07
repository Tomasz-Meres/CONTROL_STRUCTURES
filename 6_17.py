###
# A program that convert time in 24-hour format to 12-hour format
# the time in 24-hour format (hh:mm)
#

time_24 = input('Enter time (24-hour format) ')
hour_24 = int(time_24[:2])
minutes = time_24[3:5]


if hour_24 == 12 and minutes == '00':
    print(f'Time in 12-hour format: {hour_24}:{minutes} PM')
elif 12 <= hour_24 <= 23:
    print(f'Time in 12-hour format: {hour_24 - 12}:{minutes} PM')
elif hour_24 == 24 and minutes == '00':
    print(f'Time in 12-hour format: {hour_24 - 12}:{minutes} AM')
elif hour_24 < 12:
    print(f'Time in 12-hour format: {hour_24}:{minutes} AM')
else:
    print('Incorrect data')
