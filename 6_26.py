###
# A program that checks if the PIN code entered in the payment terminal is correct
#

pin = '0805'
errors = 0

while True:
    if errors < 3:
        entered_pin = input('Enter the PIN code: ')
        if entered_pin != pin:
            print('Incorrect...')
            errors += 1
    else:
        print('Sorry, your payment card has been blocked.')
        break
