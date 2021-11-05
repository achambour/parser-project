#!/usr/local/bin/python

import sys
from lexer import TokenStack
from parser import Syntax

if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        tokens = TokenStack()
        tokens.tokenize(input)