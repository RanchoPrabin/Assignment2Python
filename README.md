# Assignment2Python
#Team work for doing assignement
# ast we have to define a function to encrypt  text
qustion 1
def encrypt_text(text, shift1, shift2):
    result = ""

    for ch in text:
        if ch.islower():
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            else:
                shift = shift1 + shift2
                result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

        elif ch.isupper():
            if 'A' <= ch <= 'M':
                shift = shift1
                result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
             #### 😂😂 Cant we use 65 in place of ord('65')
            else:
                shift = shift2 ** 2
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

        else:
            result += ch

    return result


def decrypt_text(text, shift1, shift2):
    result = ""

    for ch in text:
        if ch.islower():
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
                result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            else:
                shift = shift1 + shift2
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

        elif ch.isupper():
            if 'A' <= ch <= 'M':
                shift = shift1
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                shift = shift2 ** 2
                result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))

        else:
            result += ch

    return result


def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r") as f:
        text = f.read()

    encrypted = encrypt_text(text, shift1, shift2)

    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)


def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r") as f:
        text = f.read()

    decrypted = decrypt_text(text, shift1, shift2)

    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)


def verify():
    with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
        if f1.read() == f2.read():
            print("Decryption successful")
        else:
            print("Decryption failed")


if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify()
