"""
Secret Messages.

This is secret messages.abs
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

# I was looking for the syntax to evaluate the encrpytion key as an integer
# I did consult stackoverflow for the syntax, however I can't paste into atom
# to include the link
print('Encrypt or Decrypt a message using the Caesar Cipher')
print('The encryption key can be any whole number')

while True:
    try:
        key = int(input('Please enter an encryption key: '))
        break
    except ValueError:
        print('Please enter an integer')

message = input('Please enter a message: ')
message = message.lower()

crypt = ''

while crypt not in ('E', 'D'):
    crypt = str(input('(E)ncrypt or (D)ecrypt: '))
    if crypt not in ('E', 'D'):
        print("Please enter 'E' or 'D'")

if crypt in ('E'):
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            # print(position)
            newPosition = (position + key) % 26
            # print(newPosition)
            newCharacter = alphabet[newPosition]
            # print('The new character is: ', newCharacter)
            newMessage += newCharacter
        else:
            newMessage += character
else:
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            # print(position)
            newPosition = (position - key) % 26
            # print(newPosition)
            newCharacter = alphabet[newPosition]
            # print('The new character is: ', newCharacter)
            newMessage += newCharacter
        else:
            newMessage += character

print('Your new message is: ', newMessage)
