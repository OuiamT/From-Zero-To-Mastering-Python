"""***** ENCRYPTION *****"""

# Input
# 'Tell "JACK" that the "CAT" is out the "GARDEN"!'
# Enter the shift number:

# Needed Output:
# 'Whoo "MDFN" wkdw wkh "FDW" lv rxw wkh "JDUGHQ"!' --> with shift number 3

import string


def encrypted(message, shift):
    encrypted_sentance = ""
    alphabet = string.ascii_letters

    for character in message:
        if character in alphabet:
            old_index = alphabet.index(character)
            new_index = (old_index + shift) % 52
            encrypted_sentance += alphabet[new_index]

        else:
            encrypted_sentance += character

    print(f"\nThe new sentance after encrpting is:\n{encrypted_sentance}")


sentance = input("Enter your sentance:\n").strip()
number = int(input("Enter a shift number:\t"))

encrypted(message=sentance, shift=number)
print("-" * 20)
print()


"""***** DECRYPTION *****"""

# Input
# 'Whoo "MDFN" wkdw wkh "FDW" lv rxw wkh "JDUGHQ"!'
# Enter the shift number: the same shift number

# Needed Output:
# 'Tell "JACK" that the "CAT" is out the "GARDEN"!'

import string


def encrypted(message, shift):
    dencrypted_sentance = ""
    alphabet = string.ascii_lowercase

    for character in message:
        if character.lower() in alphabet:
            old_index = alphabet.index(character.lower())
            new_index = (old_index - shift) % 26
            dencrypted_letter = alphabet[new_index]

            if character.isupper():
                dencrypted_letter = dencrypted_letter.upper()

            dencrypted_sentance += dencrypted_letter

        else:
            dencrypted_sentance += character

    print(
        f"""\nHere is the original message
*******
{dencrypted_sentance}
*******"""
    )


sentance = input("Enter your encrypted sentance:\n").strip()
number = int(input("Enter a shift number:\t"))

encrypted(message=sentance, shift=number)
