###
# A program that checks whether the EAN-13 number entered from
# keyboard consists exactly 13 digits. Additionsally, only when
# the article number is correct print a message when the product
# was manufactured in Poland
#

EAN_13 = input('Enter EAN-13 article number: ')
if len(EAN_13) == 13 and EAN_13.isdigit():
    print('Article number is correct')
    if EAN_13[:3] == '590':
        print('Article manufactured in Poland')
