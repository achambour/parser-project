import re


class Token():

    END_OF_INPUT = -1
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


class TokenStack():
    def __init__(self):
        self.tokens = list()
        self.index = 0

    def peek(self):
        return self.tokens[self.index]

    def is_at_end(self):
        return self.peek().kind == Token.END_OF_INPUT

    def eat(self):
        token = self.peek()
        if not self.is_at_end():
            self.index += 1
        return token

    def add(self, token):
        self.tokens.append(token)

    def check(self, type):
        if not self.is_at_end():
            return False
        return self.peek().kind == type

    def match(self, *tokens):
        for token in tokens:
            if self.check(token):
                return True
        return False

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
                print(f"Lexer error: unrecognized token {word}")
                exit(-1)

        self.add(Token("$", Token.END_OF_INPUT))