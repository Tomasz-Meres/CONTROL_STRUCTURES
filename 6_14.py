###
# A program that checks whether a given person is a good influencer
# Good influencer at least has two of the following accounts, Faceboook, Twitter, Instagram
#

facebook = True
twitter = False
instagram = True

print(f'facebook = {facebook}')
print(f'twitter = {twitter}')
print(f'instagram = {instagram}')
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print('You are a good influencer!')

