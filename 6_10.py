###
# Program that calculates a dog's age in dog's year.
# For the first two years, a dog's life is equal to 10.5 human years
# After that, each dog year is equal to 4 human years
#

human_years = int(input('Enter the dog\'s age in human years: '))
dogs_years = 0

if 1 <= human_years <= 2:
    dogs_years = 10.5 * human_years
elif human_years > 2:
    dogs_years = 21 + 4 * (human_years - 2)

print(f'The dog\' age in dog\'s years is {dogs_years}')
