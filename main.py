#!/usr/local/bin/python

import sys
from lexer import TokenStack
from parse import Syntax

if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        tokens = TokenStack()
        tokens.tokenize(input)

        parse = Syntax(tokens)
        root = parse.expr()

        print(root)