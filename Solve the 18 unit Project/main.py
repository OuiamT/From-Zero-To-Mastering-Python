"""
Personalized Letter Generator

This script automates the creation of personalized invitation letters.
It reads a template letter and a list of invited names, then generates
a separate customized letter for each person.

How It Works
------------
1. Reads a starting letter template from a text file.
2. Reads a list of invited names from another text file.
3. Replaces placeholder words in the template:
   - "name" → invited person's name
   - "signature" → predefined signature
4. Writes a new personalized letter for each name into an output folder.

Files Used
----------
- LETTER_PATH : Path to the letter template file.
- NAMES_PATH  : Path to the list of invited names.
"""
SIGNATURE = "OctuCode"
NAMES_PATH = r"Project\Names\Invited_names.txt"
LETTER_PATH = r"Project\Input\Starting_letter.txt"


def read_my_letter():
    with open(LETTER_PATH) as read_file:
        return read_file.read()


def read_names():
    with open(NAMES_PATH) as read_names:
        return [X.strip() for X in read_names.readlines()]


template = read_names()
for x in range(len(template)):
    with open(
        f"Project\Ready_to_send\letter_to_{template[x].lower()}.txt", "w"
    ) as my_file:
        my_file.write(
            read_my_letter()
            .replace("name", template[x])
            .replace("signature", SIGNATURE)
        )
        print(f"I type the {template[x]} letter")
