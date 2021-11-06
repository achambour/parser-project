from enum import Enum


class Token():

    EPSILON = -1
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    ASTERISK = 3
    SLASH = 4
    LPAR = 5
    RPAR = 6

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

    def number(self, arg):
        num = ""
        for c in arg:
            if not c.isdigit():
                break
            num += c
        return Token(num, Token.NUMBER)

    def symbol(self, arg):
        if arg[0] == "+":
            return Token("+", Token.PLUS)
        elif arg[0] == "-":
            return Token("-", Token.MINUS)
        elif arg[0] == "*":
            return Token("*", Token.ASTERISK)
        elif arg[0] == "/":
            return Token("/", Token.SLASH)
        elif arg[0] == "(":
            return Token("(", Token.LPAR)
        elif arg[0] == ")":
            return Token(")", Token.RPAR)

    def scan(self, arg):
        i = 0
        while i < len(arg):
            # skip blanks
            while i < len(arg) and arg[i].isspace():
                i += 1

            token = None

            # dispatch to scanner helper functions
            if arg[i].isdigit():
                token = self.number(arg[i:-1])
            elif arg[i] in "+-*/()":
                token = self.symbol(arg[i:-1])

            # add token and advance the scanner head
            if token:
                self.tokens.add(token)
                i += len(token.text)
            else:
                raise ScanningError(arg[i])

        self.tokens.add(Token("$", Token.EPSILON))