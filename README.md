
#HIT137 Assignment 2 – Question 1
#Encryption and Decryption Program

import string
import os

# Get the folder where the python file is located
base_path = os.path.dirname(os.path.abspath(__file__))

# File paths (same folder as script)
raw_file = os.path.join(base_path, "rawtext.txt")
encrypted_file = os.path.join(base_path, "encrypted_text.txt")
decrypted_file = os.path.join(base_path, "decrypted_text.txt")


# Function to shift characters
def shift_char(c, shift, alphabet):
    index = alphabet.index(c)
    new_index = (index + shift) % 26
    return alphabet[new_index]


# Encryption function
def encrypt_file(shift1, shift2):

    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()

    encrypted = ""

    for ch in text:

        if ch.islower():

            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
                encrypted += shift_char(ch, shift, string.ascii_lowercase)

            else:
                shift = -(shift1 + shift2)
                encrypted += shift_char(ch, shift, string.ascii_lowercase)

        elif ch.isupper():

            if 'A' <= ch <= 'M':
                shift = -shift1
                encrypted += shift_char(ch, shift, string.ascii_uppercase)

            else:
                shift = shift2 ** 2
                encrypted += shift_char(ch, shift, string.ascii_uppercase)

        else:
            encrypted += ch

    with open(encrypted_file, "w", encoding="utf-8") as f:
        f.write(encrypted)


# Decryption function
def decrypt_file(shift1, shift2):

    with open(encrypted_file, "r", encoding="utf-8") as f:
        text = f.read()

    decrypted = ""

    for ch in text:

        if ch.islower():

            if 'a' <= ch <= 'm':
                shift = -(shift1 * shift2)
                decrypted += shift_char(ch, shift, string.ascii_lowercase)

            else:
                shift = (shift1 + shift2)
                decrypted += shift_char(ch, shift, string.ascii_lowercase)

        elif ch.isupper():

            if 'A' <= ch <= 'M':
                shift = shift1
                decrypted += shift_char(ch, shift, string.ascii_uppercase)

            else:
                shift = -(shift2 ** 2)
                decrypted += shift_char(ch, shift, string.ascii_uppercase)

        else:
            decrypted += ch

    with open(decrypted_file, "w", encoding="utf-8") as f:
        f.write(decrypted)


# Verify if original and decrypted files match
def verify_files():

    with open(raw_file, "r", encoding="utf-8") as f1:
        original = f1.read()

    with open(decrypted_file, "r", encoding="utf-8") as f2:
        decrypted = f2.read()

    if original == decrypted:
        print("Decryption successful: Files match")
    else:
        print("Decryption failed: Files do not match")


# Main program
print("=== Text Encryption Program ===")

shift1 = int(input("Enter shift1 value: "))
shift2 = int(input("Enter shift2 value: "))

encrypt_file(shift1, shift2)
print("Encryption completed")

decrypt_file(shift1, shift2)
print("Decryption completed")

verify_files()


## question 2

