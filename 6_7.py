###
# A program that ask the user for their age and then checks
# which age group they belong to Child: under 13, Teen: 13 to 19,
# Adult 20 to 64, Senior 65 or older
#

age = int(input('Enter your age: '))

if age < 13:
    print('You belong to children group')
elif 13 <= age <= 19:
    print('You belong to teen group')
elif 20 <= age <= 64:
    print('You belong to adult group')
elif age > 65:
    print('You belong to senior group')
