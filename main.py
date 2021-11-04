#!/usr/local/bin/python

import sys
import lexer

if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        tokens = lexer.Tokenizer()
        tokens.tokenize(input)

        token = tokens.head

        while token:
            if token.prev:
                print(f"Previous: {token.prev.text}")
            print(f"Token: {token.text}")
            if token.next:
                print(f"Next: {token.next.text}")
            print("\n")
            token = token.next