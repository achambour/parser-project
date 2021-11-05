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
        self.next = None

    def match(self, *tokens):
        for token in tokens:
            if self.check(token):
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

    def insert_end(self, new):
        # first token inserted
        if not self.head and not self.tail:
            self.head = new
            self.tail = new
            return

        self.tail.next = new
        self.tail = new

    def tokenize(self, input):
        for word in input.split():
            if word.isnumeric():
                self.insert_end(Token(word, Token.NUMBER))
            elif word in "+":
                self.insert_end(Token(word, Token.PLUS))
            elif word in "-":
                self.insert_end(Token(word, Token.MINUS))
            elif word in "*":
                self.insert_end(Token(word, Token.STAR))
            elif word in "/":
                self.insert_end(Token(word, Token.SLASH))
            elif word == "(":
                self.insert_end(Token(word, Token.LPAR))
            elif word == ")":
                self.insert_end(Token(word, Token.RPAR))
            else:
                print(f"Error: lexer: unrecognized token {word}")
                exit(-1)

        self.insert_end(Token("$", Token.EOF))