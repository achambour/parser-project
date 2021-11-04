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


class Syntax():
    def __init__(self, start_token):
        self.token = start_token

    def expr(self):
        return self.term()

    def term(self):
        expr = self.factor()

        while self.token.match(lexer.PLUS, lexer.MINUS):
            operator = self.token
            self.token = self.token.next
            right = self.factor()
            # expr = subtree.term(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.token.match(lexer.STAR, lexer.SLASH):
            operator = self.token
            self.token = self.token.next
            right = self.unary()
            # expr = subtree.factor(expr, operator, right)

        return expr

    def unary(self):
        if self.token.match(lexer.MINUS):
            operator = self.token
            self.token = self.token.next
            right = self.unary()
            # return subtree.unary(operator, right)
            return None

        return self.primary()

    def primary(self):
        if self.token.match(lexer.LPAR):
            self.token = self.token.next
            expr = self.expr()

            if not self.token.match(lexer.RPAR):
                print(f"Error: parser: expect ')' after expression")
                exit(-1)

            # return subtree.grouping(expr)
            return None

        if self.token.match(lexer.NUMBER):
            # return subtree.number(self.token)
            return None
