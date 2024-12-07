###
# A program that prints a survey consisting of three questions
#

print('SURVEY')
question1 = input('Are you interested in computer science? (y/n) ')
question2 = input('Do you like playing computer games? ')
question3 = input('Do you have an Instagram account? (y/n) ')
answer1 = 'No'
answer2 = 'No'
answer3 = 'No'

if question1 == 'y':
    answer1 = 'Yes'
if question2 == 'y':
    answer2 = 'Yes'
if question3 == 'y':
    answer3 = 'Yes'

print('SURVEY RESULTS')
print(f'Interested in computer science: {answer1}')
print(f'Playing computer games: {answer2}')
print(f'Has an Instagram account: {answer3}')
