import re


class Token():

    EOF = -1
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    STAR = 3
    SLASH = 4
    LPAR = 5
    RPAR = 6

    def __init__(self, text, kind):
        self.text = text
        self.kind = kind
        self.prev = None
        self.next = None

    def match(self, *args):
        for kind in args:
            if self.check(kind):
                return True
        return False

    def check(self, kind):
        if self.kind == self.EOF:
            return False

        # peek current token
        return self.kind == kind


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
                self.add(Token(word, Token.NUMBER))
            elif word in "+":
                self.add(Token(word, Token.PLUS))
            elif word in "-":
                self.add(Token(word, Token.MINUS))
            elif word in "*":
                self.add(Token(word, Token.STAR))
            elif word in "/":
                self.add(Token(word, Token.SLASH))
            elif word == "(":
                self.add(Token(word, Token.LPAR))
            elif word == ")":
                self.add(Token(word, Token.RPAR))
            else:
                print(f"Error: lexer: unrecognized token {word}")
                exit(-1)

        self.add(Token("$", Token.EOF))