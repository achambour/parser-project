#!/usr/bin/env python3

import sys
from lexer import TokenStack
from parse import Syntax

import pydot


def traverse_inorder(graph, node):
    if node:
        traverse_inorder(graph, node.left)
        if node.left:
            graph.add_edge(pydot.Edge(id(node.token), id(node.left.token)))
        if node.right:
            graph.add_edge(pydot.Edge(id(node.token), id(node.right.token)))
        traverse_inorder(graph, node.right)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        input = str(sys.argv[1])

        tokens = TokenStack()
        tokens.tokenize(input)

        parse = Syntax(tokens)
        root = parse.expr()

        traverse_inorder(parse.graph, root)

        parse.graph.write_png("output.png")
