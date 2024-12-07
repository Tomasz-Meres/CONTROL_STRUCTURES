###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char == ' ':
        encrypted_text = encrypted_text + ' '
        continue
    # read the characters code
    number = ord(char)
    # add one to the  character's code
    crypted_number = number + 1
    # replace new character code with its
    # corresponding character
    letter = chr(crypted_number)
    # add encrypted character to text
    encrypted_text = encrypted_text + letter

print(plain_text)
print(encrypted_text)
