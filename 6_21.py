###
# A program showing any amount (natural number) read from the keyboard
# with as few coins as possible
#

amount = int(input('Enter amount on PLN: '))
coin_5 = 0
coin_2 = 0
coin_1 = 0

while amount > 0:
    if amount >= 5:
        coin_5 += 1
        amount -= 5
    elif 2 <= amount < 5:
        coin_2 += 1
        amount -= 2
    else:
        coin_1 += 1
        amount -= 1

print(f'The amount of PLN {amount} in coins')
print(f'5 PLN coins: {coin_5}')
print(f'2 PLN coins: {coin_2}')
print(f'1 PLN coins: {coin_1}')
