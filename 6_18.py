###
# A program that determines in which quadrant of the coordinate
# system the point P(x, y) is located or on which axis it is located
# or that is located  in position (0,0)
#

x = int(input('Enter position of x: '))
y = int(input('Enter position of y: '))

if x == 0 and y == 0:
    print(f'Point({x},{y})')
elif x == 0:
    print(f'Point({x},{y}) is on the y-axis')
elif y == 0:
    print(f'Point({x},{y}) is on the x-axis')

if x > 0 and y > 0:
    print(f'Point({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point({x},{y}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point({x},{y}) is in the fourth quadrant of the coordinate system')
