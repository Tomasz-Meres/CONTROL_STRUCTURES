i = 6
j = 1

while i >= 0:
    while j < 4:
        print(f'{i+j}', end=' ')
        j += 1
    if i - 3 >= 0:
        print('')
    i -= 3
    j = 1
