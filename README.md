
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
import re
import os
# automatically detect folder of the script
base_path = os.path.dirname(os.path.abspath(_file_))
imput_file = os.path.join(base_path,"sample_input.txt")
output_file = os.path.join(base_path,"output.txt")
#---------
# TOKENIZER
#----------
def tokenize(exp):
token pattern = r'\d+|[()+\-*/]'
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
     -----------------------------
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


