
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



## question 2
import re
import os
# automatically detect folder of the script
base_path = os.path.dirname(os.path.abspath(_file_))
imput_file = os.path.join(base_path,"sample_input.txt")
output_file = os.path.join(base_path,"output.txt")
#---------
# TOKENIZER
# -----------------------------
def tokenize(expr):

    # check for invalid characters
    if re.search(r'[^\d+\-*/()\s]', expr):
        raise Exception("Invalid character")

    token_pattern = r'\d+|[()+\-*/]'
    parts = re.findall(token_pattern, expr)

    tokens = []

    for p in parts:

        if p.isdigit():
            tokens.append(("NUM", p))

        elif p in "+-*/":
            tokens.append(("OP", p))

        elif p == "(":
            tokens.append(("LPAREN", p))

        elif p == ")":
            tokens.append(("RPAREN", p))

    tokens.append(("END", ""))

    return tokens
# PARSER
# -----------------------------
class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self):
        self.pos += 1

    def parse(self):
        return self.expr()

    def expr(self):

        node = self.term()

        while self.current()[1] in ("+", "-"):
            op = self.current()[1]
            self.eat()
            right = self.term()
            node = (op, node, right)

        return node

    def term(self):

        node = self.factor()

        while self.current()[1] in ("*", "/"):
            op = self.current()[1]
            self.eat()
            right = self.factor()
            node = (op, node, right)

        return node

    def factor(self):

        token = self.current()

        if token[0] == "NUM":
            self.eat()
            return int(token[1])

        if token[1] == "-":
            self.eat()
            operand = self.factor()
            return ("neg", operand)

        if token[0] == "LPAREN":
            self.eat()
            node = self.expr()
            self.eat()
            return node

        raise Exception("Parse error")


# -----------------------------
# TREE STRING
# -----------------------------
def tree_to_string(node):

    if isinstance(node, int):
        return str(node)

    if node[0] == "neg":
        return f"(neg {tree_to_string(node[1])})"

    op, left, right = node
    return f"({op} {tree_to_string(left)} {tree_to_string(right)})"


# -----------------------------
# EVALUATOR
# -----------------------------
def evaluate(node):

    if isinstance(node, int):
        return node

    if node[0] == "neg":
        return -evaluate(node[1])

    op, left, right = node

    l = evaluate(left)
    r = evaluate(right)

    if op == "+":
        return l + r

    if op == "-":
        return l - r

    if op == "*":
        return l * r

    if op == "/":
        if r == 0:
            raise Exception("Divide by zero")
        return l / r


        

Assignment 2 done by jeetika 
here I am writing the code that i will be using to do the assignment 

 def shift_char(char, shift):
    """Shift a character within alphabet range using wrap-around."""
    if 'a' <= char <= 'z':
        start = ord('a')
        return chr((ord(char) - start + shift) % 26 + start)
    elif 'A' <= char <= 'Z':
        start = ord('A')
        return chr((ord(char) - start + shift) % 26 + start)
    return char

    Encryption Function
    def encrypt_text(text, shift1, shift2):
    encrypted = ""

    for ch in text:
        if 'a' <= ch <= 'm':
            encrypted += shift_char(ch, shift1 * shift2)
        elif 'n' <= ch <= 'z':
            encrypted += shift_char(ch, -(shift1 + shift2))
        elif 'A' <= ch <= 'M':
            encrypted += shift_char(ch, -shift1)
        elif 'N' <= ch <= 'Z':
            encrypted += shift_char(ch, shift2 ** 2)
        else:
            encrypted += ch

    return encrypted  

Decryption Function
    
def decrypt_text(text, shift1, shift2):
    decrypted = ""

    for ch in text:
        if 'a' <= ch <= 'm':
            decrypted += shift_char(ch, -(shift1 * shift2))
        elif 'n' <= ch <= 'z':
            decrypted += shift_char(ch, shift1 + shift2)
        elif 'A' <= ch <= 'M':
            decrypted += shift_char(ch, shift1)
        elif 'N' <= ch <= 'Z':
            decrypted += shift_char(ch, -(shift2 ** 2))
        else:
            decrypted += ch

    return decrypted

##Decryption Function

def decrypt_text(text, shift1, shift2):
    decrypted = ""

    for ch in text:
        if 'a' <= ch <= 'm':
            decrypted += shift_char(ch, -(shift1 * shift2))
        elif 'n' <= ch <= 'z':
            decrypted += shift_char(ch, shift1 + shift2)
        elif 'A' <= ch <= 'M':
            decrypted += shift_char(ch, shift1)
        elif 'N' <= ch <= 'Z':
            decrypted += shift_char(ch, -(shift2 ** 2))
        else:
            decrypted += ch

    return decrypted



##File Encryption Function

def encrypt_file(input_file, output_file, shift1, shift2):
    with open(input_file, "r", encoding="utf-8") as f:
        raw_text = f.read()

    encrypted = encrypt_text(raw_text, shift1, shift2)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted)

    print(f"Encrypted text written to {output_file}")
    
Verification Function
def verify_files(original_file, decrypted_file):
    with open(original_file, "r", encoding="utf-8") as f:
        original_text = f.read()

    with open(decrypted_file, "r", encoding="utf-8") as f:
        decrypted_text = f.read()

    if original_text == decrypted_text:
        print("Verification successful: Decrypted text matches the original.")
    else:
        print("Verification failed: Decrypted text does NOT match the original.")

##Main Function
def main():
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
    except ValueError:
        print("Please enter valid integer values for shift1 and shift2.")
        return

    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    encrypt_file(raw_file, encrypted_file, shift1, shift2)
    decrypt_file(encrypted_file, decrypted_file, shift1, shift2)
    verify_files(raw_file, decrypted_file)

   ## Program Execution
if __name__ == "__main__":
    main()
    
        

