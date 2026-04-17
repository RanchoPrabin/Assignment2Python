
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




## Question 2


import re
import os


# automatically detect folder of the script
base_path = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(base_path, "sample_input.txt")
output_file = os.path.join(base_path, "output.txt")


# TOKENIZER

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


# TREE STRING

def tree_to_string(node):

    if isinstance(node, int):
        return str(node)

    if node[0] == "neg":
        return f"(neg {tree_to_string(node[1])})"

    op, left, right = node
    return f"({op} {tree_to_string(left)} {tree_to_string(right)})"



# EVALUATOR

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


# MAIN PROCESS

def evaluate_file():

    if not os.path.exists(input_file):
        print("Input file not found:", input_file)
        return

    with open(input_file) as f:
        lines = f.readlines()

    out = open(output_file, "w")

    for line in lines:

        expr = line.strip()

        if expr == "":
            continue

        try:

            tokens = tokenize(expr)

            parser = Parser(tokens)

            tree = parser.parse()

            result = evaluate(tree)

            tree_str = tree_to_string(tree)

            token_str = " ".join(
                [f"[{t[0]}:{t[1]}]" if t[1] else "[END]" for t in tokens]
            )

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 4)

        except:

            tree_str = "ERROR"
            token_str = "ERROR"
            result = "ERROR"

        out.write(f"Input: {expr}\n")
        out.write(f"Tree: {tree_str}\n")
        out.write(f"Tokens: {token_str}\n")
        out.write(f"Result: {result}\n\n")

    out.close()

    print("Finished. Check output.txt")


# run program
evaluate_file()
