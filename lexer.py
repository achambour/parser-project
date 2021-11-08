from enum import Enum


class Token():

    EPSILON = -1
    PLUS = 0
    MINUS = 1
    ASTERISK = 2
    SLASH = 3
    LPAR = 4
    RPAR = 5
    NUMBER = 6

    def __init__(self, text, kind):
        self.text = text
        self.kind = kind


class TokenStack():
    def __init__(self):
        self.tokens = []
        self.index = 0

    def peek(self):
        return self.tokens[self.index]

    def is_at_end(self):
        return self.peek().kind == Token.EPSILON

    def eat(self):
        token = self.peek()
        if not self.is_at_end():
            self.index += 1
        return token

    def add(self, token):
        self.tokens.append(token)

    def check(self, type):
        if self.is_at_end():
            return False
        return self.peek().kind == type

    def match(self, *tokens):
        for token in tokens:
            if self.check(token):
                return True
        return False


class ScanningError(Exception):
    def __init__(self, character):
        super().__init__(f"Scanning error: unrecognized token '{character}'")


class Tokenizer():
    def __init__(self):
        self.tokens = TokenStack()

    def scan(self, str):
        i = 0
        n = len(str)
        while i < n:
            if str[i].isspace():
                while i < n and str[i].isspace():
                    i += 1
            elif str[i].isnumeric():
                s = ""
                while i < n and str[i].isnumeric():
                    s += str[i]
                    i += 1
                self.tokens.add(Token(s, Token.NUMBER))
            elif str[i] == "+":
                self.tokens.add(Token("+", Token.PLUS))
                i += 1
            elif str[i] == "-":
                self.tokens.add(Token("-", Token.MINUS))
                i += 1
            elif str[i] == "*":
                self.tokens.add(Token("*", Token.ASTERISK))
                i += 1
            elif str[i] == "/":
                self.tokens.add(Token("/", Token.SLASH))
                i += 1
            elif str[i] == "(":
                self.tokens.add(Token("(", Token.LPAR))
                i += 1
            elif str[i] == ")":
                self.tokens.add(Token(")", Token.RPAR))
                i += 1
            else:
                raise Exception(f"Lexer: unrecognized token {str[i]}")
        self.tokens.add(Token("$", Token.EPSILON))
