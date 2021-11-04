import re


class Token():

    NUMBER = 0
    OPERATOR = 1
    LEFTPAR = 2
    RIGHTPAR = 3

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
                self.add(Token(word, Token.NUMBER))
            elif word in "+-*/":
                self.add(Token(word, Token.OPERATOR))
            elif word == "(":
                self.add(Token(word, Token.LEFTPAR))
            elif word == ")":
                self.add(Token(word, Token.RIGHTPAR))
            else:
                print(f"Error: lexer: unrecognized token {word}")
                exit(-1)