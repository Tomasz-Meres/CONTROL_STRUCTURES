###
# Program that simulates the operation of an electronic thermometer
#

temperature = 32
if temperature > 35:
    print('It is extremely hot')
elif 35 >= temperature > 30:
    print('It is hot')
elif 30 >= temperature >= 15:
    print('It is warm')
elif 15 > temperature >= 0:
    print('It is cold')
else:
    print('Warning frost')
