
##HIT137 Assignment 2 Question 
##Encryption and Decryption Program


import os


# FILE PATH SETUP

base_path = os.path.dirname(os.path.abspath(__file__))

raw_file = os.path.join(base_path, "raw_text.txt")
encrypted_file = os.path.join(base_path, "encrypted_text.txt")
decrypted_file = os.path.join(base_path, "decrypted_text.txt")



# ENCRYPTION
def encrypt_char(ch, shift1, shift2): #Function

    if ch.islower():
        offset = ord(ch) - ord('a')

        # For Range a-m
        if offset <= 12:
            new_offset = (offset + shift1 * shift2) % 26

        # For Range n-z
        else:
            new_offset = (offset - (shift1 + shift2)) % 26

        return chr(ord('a') + new_offset)

    elif ch.isupper():
        offset = ord(ch) - ord('A')

        # For Range A-M
        if offset <= 12:
            new_offset = (offset - shift1) % 26

        # For Range N-Z
        else:
            new_offset = (offset + shift2 ** 2) % 26

        return chr(ord('A') + new_offset)

    else:
        return ch


# DECRYPTION

def decrypt_char(ch, shift1, shift2): #Function

    if ch.islower():
        enc_off = ord(ch) - ord('a')

        # Try inverse of a-m range
        candidate1 = (enc_off - shift1 * shift2) % 26
        if 0 <= candidate1 <= 12:
            return chr(ord('a') + candidate1)

        # Try inverse of n-z range
        candidate2 = (enc_off + shift1 + shift2) % 26
        if 13 <= candidate2 <= 25:
            return chr(ord('a') + candidate2)

        return chr(ord('a') + candidate1)

    elif ch.isupper():
        enc_off = ord(ch) - ord('A')

        # Try inverse of A-M range
        candidate1 = (enc_off + shift1) % 26
        if 0 <= candidate1 <= 12:
            return chr(ord('A') + candidate1)

        # Try inverse of N-Z range
        candidate2 = (enc_off - shift2 ** 2) % 26
        if 13 <= candidate2 <= 25:
            return chr(ord('A') + candidate2)

        # fallback
        return chr(ord('A') + candidate1)

    else:
        return ch


# ENCRYPT FILE
def encrypt_file(shift1, shift2): ##Fuction call

    with open(raw_file, "r", encoding="utf-8") as f:
        text = f.read()

    encrypted = "".join(encrypt_char(ch, shift1, shift2) for ch in text)

    with open(encrypted_file, "w", encoding="utf-8") as f: ##file path
        f.write(encrypted)

    print("Encryption complete: encrypted_text.txt")


# DECRYPT FILE
def decrypt_file(shift1, shift2):

    with open(encrypted_file, "r", encoding="utf-8") as f:
        text = f.read()

    decrypted = "".join(decrypt_char(ch, shift1, shift2) for ch in text)

    with open(decrypted_file, "w", encoding="utf-8") as f:
        f.write(decrypted)

    print("Decryption complete: decrypted_text.txt")


# VERIFY FUNCTION

def verify_files():

    with open(raw_file, "r", encoding="utf-8") as f1:
        original = f1.read()

    with open(decrypted_file, "r", encoding="utf-8") as f2:
        decrypted = f2.read()

    if original == decrypted: ## Checking decrypted file with original file
        print(" Decryption is successful and  original file is matched ")
    else:
        print(" Decryption is failed:")


# MAIN PROGRAM


shift1 = int(input("Enter shift1 value: "))
shift2 = int(input("Enter shift2 value: "))

encrypt_file(shift1, shift2)
decrypt_file(shift1, shift2)
verify_files()
