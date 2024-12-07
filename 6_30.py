###
# A program that prints a lottery coupon
#

for i in range(1, 8):
    for j in range(0, 49, 7):
        print(f'{i+j}', end=' ')

    print('')
