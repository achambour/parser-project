from lexer import Token
'''
The grammar must be predictive (at least by one token of lookahead in our case)
otherwise the parser cannot select the appropriate expansion rule.

A parser that implements backtracking in the combinatorial sense of constructing
the parse tree associated with the grammar to explore all the possibilities that
the grammar can accept is named LL(*) with "infinite" lookahead and is extremely
inefficient, so we selected a predictive LL(1) recursive descent parser instead.

Our grammar must be unambiguous, that is, for a given input only a single parse
tree can be derived.

Ambiguity is dangerous as it introduces undecidability in our algorithm. We can
often fix the ambiguity by adding prededence rules or context-sensitive code in
the parser.

Luckily, our grammar is unambiguous. But we still need operator precedence as we
are implementing a calculator.

Precedence is from lowest to highest (same as in C):

expr    -> term
term    -> term ("+" | "-") factor | factor
factor  -> factor ("*" | "/") unary | unary
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $

LL grammars (parsed from top-down) are subjective to the left recursion problem.

Indeed, our grammar will cause infinite recursion in a recursive-descent parser:

def term():
    term()  # Oops

And is eliminated by refactoring left recursive rules into right recursive ones:

expr    -> term
term    -> factor ("+" | "-") factor | factor
factor  -> unary ("*" | "/") unary | unary
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $

Simplifying:

expr    -> term
term    -> factor ( ("+" | "-") factor )*
factor  -> unary ( ("*" | "/") unary )*
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $

Where the grammar notation yield the following code implementation:

Terminal    -> match and eat a token
Nonterminal -> call to the corresponding rule function
|           -> if or switch (or peek current token to choose an expansion rule)
* or +      -> while or for loop to match the regex group
?           -> if condition (match and eat a token only if present)
'''


class Parser():
    def __init__(self, tokens):
        self.tokens = tokens

    def expr(self):
        self.term()

    def term(self):
        left = self.factor()
        while self.tokens.match(Token.PLUS, Token.MINUS):
            operator = self.tokens.pop()
            right = self.factor()
            # expr = Infix(left, operator, right)
        return None

    def factor(self):
        left = self.unary()
        while self.tokens.match(Token.STAR, Token.SLASH):
            operator = self.tokens.pop()
            right = self.unary()
            # expr = Infix(left, operator, right)
        return None

    def unary(self):
        if self.tokens.match(Token.MINUS):
            operator = self.tokens.pop()
            right = self.unary()
            # return Unary(operator, right)
        return self.primary()

    def primary(self):

        if self.tokens.match(Token.LPAR):
            self.tokens.pop()
            expr = self.expr()
            if self.tokens.match(Token.RPAR):
                self.tokens.pop()
                # return NestedGroup(expr)
                return None
            else:
                print("Parse error: expect ')' after expression")

        if self.tokens.match(Token.NUMBER):
            number = self.tokens.pop()
            # return NumberLiteral(number)
            return None

        return None
