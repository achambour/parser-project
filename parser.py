import lexer
'''

Precedence is from lowest to highest (same as C):

expr    -> term
term    -> term ("+" | "-") factor | factor
factor  -> factor ("*" | "/") unary | unary
unary   -> "-" unary | primary
primary -> "(" expr ")" | [0-9] | $

Such a grammar would cause infinite recursion in a recursive-descent parser:

def term():
    term()  # Oops

And is eliminated with:

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

'''


class Parser():
    def __init__(self, start_token):
        self.token = start_token

    def expr(self):
        return self.term()

    def term(self):
        left = self.factor()

        while  self.token.match("+", "-"):
            operator = self.token.prev
            right = self.factor()
            # expr = subtree.term(left, operator, right);

    def factor(self):
        pass

    def unary(self):
        pass

    def primary(self):
        pass