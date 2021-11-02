#!/opt/homebrew/bin/python

import sys
from pprint import pprint

""" Lexical analysis """

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
            self.tokens.append(Token((c in self.TERMS), c))


if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        lexer = Lexer()
        lexer.tokenize(input)

        for token in lexer.tokens:
            print(f"Is it a term? {token.is_term}, value: {token.value}")
