# Python recursive-descent parser

## Context-free grammar

We want to parse arithmetic expressions to implement a small calculator. Some examples of valid expressions include:

```
2 + 3 * 5
1 + 1 + (2 - 1)
8 / 4 / 2
-1 - -1
```

The grammar must be predictive (at least by one token of lookahead in our case) otherwise the parser cannot select the appropriate expansion rule.

For an LL(1) grammar, the parser will "peek" the current token prior consuming it in order to choose the appropriate rule.

A parser that implements backtracking in the combinatorial sense of constructing the parse tree associated with the grammar to explore all the possibilities that the grammar can accept is named LL(*) with "infinite" lookahead and is extremely inefficient, so we selected a predictive recursive-descent parser instead.

Our grammar must be unambiguous, that is, for a given input only a single parse tree can be derived. Ambiguity introduces undecidability and the parser must be a deterministic finite state machine. We need to solve the ambiguity to implement our parsing algorithm, as the parser cannot decice on its own.

```
expr    ⟶ term
term    ⟶ term ("+" | "-") factor | factor
factor  ⟶ factor ("*" | "/") unary | unary
unary   ⟶ "-" unary | primary
primary ⟶ "(" expr ")" | NUMBER | $
```

We can fix the ambiguity by adding prededence rules or context-sensitive code in the parser or refactoring the grammar.

A recursive-descent parser will construct the parse tree top-down so we removed ambiguity by breaking down rules based on precedence and associativity. In our case, associativity is always left-to-right as we are parsing arithmetic expressions. Only the precedence order changes.

The precedence is from lowest to highest (same as in C):

```
expr    ⟶ term
term    ⟶ term ("+" | "-") factor | factor
factor  ⟶ factor ("*" | "/") unary | unary
unary   ⟶ "-" unary | primary
primary ⟶ "(" expr ")" | NUMBER | $
```

> Note: `NUMBER` is a token scanned by the lexer that represents a valid number input.

LL grammars (parsed from top-down) are also subject to the left recursion problem. Indeed, our grammar will cause infinite recursion in a recursive-descent parser:

```python
def term():
    left = term() # Oops
    while match("+", "-"):
        operator = eat()
        right = factor()
        expr = Infix(left, operator, right)
    return expr
```

This is fixed by refactoring each left recursive rule into a right recursive one:

```
expr    ⟶ term
term    ⟶ factor ("+" | "-") factor | factor
factor  ⟶ unary ("*" | "/") unary | unary
unary   ⟶ "-" unary | primary
primary ⟶ "(" expr ")" | NUMBER | $
```

Simplifying the grammar in a regex-like notation:

```
expr    ⟶ term
term    ⟶ factor ( ("+" | "-") factor )*
factor  ⟶ unary ( ("*" | "/") unary )*
unary   ⟶ "-" unary | primary
primary ⟶ "(" expr ")" | NUMBER | $
```

This notation yields the following code implementation:

| Grammar notation | Code implementation                                                  |
| ---------------- | -------------------------------------------------------------------- |
| Terminal         | Match and eat a token                                                |
| Nonterminal      | Call to the corresponding rule function                              |
| `\|`             | `if` or `switch` (or peek current token to choose an expansion rule) |
| `*` or `+`       | `while` or `for` loop to match the regex group                       |
| `?`              | `if` condition (match and eat a token only if present)               |


## AST

The parser will construct an abstract syntax tree (AST) to capture the semantic representation of the expression. The AST is stored as a binary tree where nodes are added by each nonterminal function of the recursive-descent parser.

The AST is implicitly derived from the parse tree, also known as the concrete syntax tree (CST), which is constructed top-down by the recursive-descent parser and follows the precedence ordering established by the grammar.

The depth-first search (DFS) algorithm is used to traverse the AST since the parse tree is constructed top-down and the AST is implicitly derived from the parse tree.

The grammar uses top-down operator precedence, where the precedence order is low to high. This is confusing: rules at the top of the grammar have a lower precedence value while rules at the bottom have an higher one.


## Useful resources

* https://cs.stackexchange.com/questions/56625/lookahead-in-llk-parsing