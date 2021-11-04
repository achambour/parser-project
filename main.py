#!/usr/local/bin/python

import sys
import lexer
import parser

if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        # Tokenize the input
        tokens = lexer.Tokenizer()
        tokens.tokenize(input)

        # Parse the expr from the start token (head)
        parser = parser.Syntax(tokens.head)
        parser.expr()