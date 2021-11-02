#!/usr/local/bin/python

import sys
from pprint import pprint


class Token():
    def __init__(self, is_term, value):
        self.is_term = is_term
        self.value = value


class Lexer():

    TERMS = {
        "+", "-", "*", "/", "(", ")", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    }

    def __init__(self):
        self.tokens = []

    def tokenize(self, input):
        for c in input:
            if c in self.TERMS:
                token = Token(True, c)
                self.tokens.append(token)
            else:
                token = Token(False, c)
                self.tokens.append(token)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        lexer = Lexer()
        lexer.tokenize(input)

        for token in lexer.tokens:
            print(f"Is it a term? {token.is_term}, value: {token.value}")