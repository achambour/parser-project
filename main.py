#!/usr/local/bin/python

import sys
from lexer import Tokenizer
from parser import Syntax

if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        # Tokenize the input
        tokens = Tokenizer()
        tokens.tokenize(input)

        # Parse the expr from the start token (head)
        parser = Syntax(tokens.head)
        parser.expr()