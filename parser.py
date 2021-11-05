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


class Syntax():
    def __init__(self, start_token):
        self.token = start_token

    # expect a token and eat it
    def eat(self, token):
        if self.token.match(token):
            self.token = self.token.next

    def expr(self):
        return self.term()

    def term(self):
        expr = self.factor()

        while self.token.match(Token.PLUS, Token.MINUS):
            print(f"Info: parser: matched '{self.token.text}'")
            operator = self.token
            self.token = self.token.next
            right = self.factor()
            # expr = subtree.term(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.token.match(Token.STAR, Token.SLASH):
            print(f"Info: parser: matched '{self.token.text}'")
            operator = self.token
            self.token = self.token.next
            right = self.unary()
            # expr = subtree.factor(expr, operator, right)

        return expr

    def unary(self):
        if self.token.match(Token.MINUS):
            print(f"Info: parser: matched '{self.token.text}'")
            operator = self.token
            self.token = self.token.next
            right = self.unary()

            # return subtree.unary(operator, right)
            return None

        return self.primary()

    def primary(self):
        if self.token.match(Token.LPAR):
            print(f"Info: parser: matched '{self.token.text}'")
            self.token = self.token.next

            # recurse back to the start symbol
            expr = self.expr()

            if self.token.match(Token.RPAR):
                print(f"Info: parser: matched '{self.token.text}'")
                self.token = self.token.next
            else:
                print(f"Error: parser: expect ')' after expression")
                exit(-1)

            # return subtree.grouping(expr)
            return None

        if self.token.match(Token.NUMBER):
            print(f"Info: parser: matched '{self.token.text}'")
            number = self.token
            self.token = self.token.next

            # return subtree.number(number)
            return None

        return None