import re

NUMBER = 0
PLUS = 1
MINUS = 2
STAR = 3
SLASH = 4
LPAR = 5
RPAR = 6


class Token():
    def __init__(self, text, kind):
        self.text = text
        self.kind = kind
        self.prev = None
        self.next = None

    def peek(self, text):
        return self.next.text == text

    def match(self, *tokens):
        for token in tokens:
            if self.kind == token:
                return True
        return False


class Tokenizer():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, new):
        # first token inserted
        if not self.head and not self.tail:
            self.head = new
            self.tail = new
            return

        self.tail.next = new
        new.prev = self.tail
        self.tail = new

    def tokenize(self, input):
        for word in input.split():
            if word.isnumeric():
                self.add(Token(word, NUMBER))
            elif word in "+":
                self.add(Token(word, PLUS))
            elif word in "-":
                self.add(Token(word, MINUS))
            elif word in "*":
                self.add(Token(word, STAR))
            elif word in "/":
                self.add(Token(word, SLASH))
            elif word == "(":
                self.add(Token(word, LPAR))
            elif word == ")":
                self.add(Token(word, RPAR))
            else:
                print(f"Error: lexer: unrecognized token {word}")
                exit(-1)