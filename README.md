# Python recursive-descent parser

We want to parse arithmetic expressions to implement a small calculator. Some examples of valid expressions include:

```
2 + 3 * 5
1 + 1 + (2 - 1)
8 / 4 / 2
-1 - -1
```

The grammar must be predictive (at least by one token of lookahead in our case) otherwise the parser cannot select the appropriate expansion rule.

A parser that implements backtracking in the combinatorial sense of constructing the parse tree associated with the grammar to explore all the possibilities that the grammar can accept is named LL(*) with "infinite" lookahead and is extremely inefficient, so we selected a predictive LL(1) recursive descent parser instead.

Our grammar must be unambiguous, that is, for a given input only a single parse tree can be derived.

Ambiguity is dangerous as it introduces undecidability in our algorithm. We can often fix the ambiguity by adding prededence rules or context-sensitive code in the parser.

Luckily, our grammar is unambiguous. But we still need operator precedence as we are implementing a calculator.

Precedence is from lowest to highest (same as in C):

```
expr    -> term
term    -> term ("+" | "-") factor | factor
factor  -> factor ("*" | "/") unary | unary
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $
```

LL grammars (parsed from top-down) are subject to the left recursion problem.

Indeed, our grammar will cause infinite recursion in a recursive-descent parser:

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
expr    -> term
term    -> factor ("+" | "-") factor | factor
factor  -> unary ("*" | "/") unary | unary
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $
```

Simplifying the grammar in a regex-like notation:

```
expr    -> term
term    -> factor ( ("+" | "-") factor )*
factor  -> unary ( ("*" | "/") unary )*
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $
```

This notation yields the following code implementation:

| Grammar notation | Code implementation                                                  |
| ---------------- | -------------------------------------------------------------------- |
| Terminal         | Match and eat a token                                                |
| Nonterminal      | Call to the corresponding rule function                              |
| `\|`             | `if` or `switch` (or peek current token to choose an expansion rule) |
| `*` or `+`       | `while` or `for` loop to match the regex group                       |
| `?`              | `if` condition (match and eat a token only if present)               |