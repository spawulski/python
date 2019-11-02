"""
Encrypter/Decrypter.

A little application that will encrypt or decrypt using the Caesar Cipher
"""

# Imports from guizero
from guizero import App, Text, TextBox, Slider, Combo, PushButton


def cipher():
    """Apply cipher to text either encrypting or deprypting."""
    """Transform text in message box based on user choice."""
    newMessage = ""
    message = message_box.value.lower()

    if encryption_choice.value == "Encrypt":
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position + key_slider.value) % 26
                newCharacter = alphabet[newPosition]
                newMessage += newCharacter
            else:
                newMessage += character

    else:
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position - key_slider.value) % 26
                newCharacter = alphabet[newPosition]
                newMessage += newCharacter
            else:
                newMessage += character

    message_box.value = newMessage


# The Alphabet as a string that we use for Caesar cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Instantiate App object along with the widgets it uses.
app = App(title="Caesar Ciper Tool", height=240)
to_be_crypted = Text(app, text="Enter the message:", size=26)
message_box = TextBox(app, width=40)
encryption_choice = Combo(app, options=["Encrypt", "Decrypt"])
key_text = Text(app, text="Use slider to select encryption key", size=24)
key_slider = Slider(app, start=1, end=25)
button = PushButton(app, command=cipher, text="Apply Cipher")
app.display()
