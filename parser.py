from lexer import Token
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

    def advance(self):
        if self.token.next:
            self.token = self.token.next

    def expr(self):
        return self.term()

    def term(self):
        expr = self.factor()

        while self.token.match(Token.PLUS, Token.MINUS):
            print(f"Info: parser: matched '{self.token.text}'")
            operator = self.token
            self.advance()
            right = self.factor()
            # expr = subtree.term(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while self.token.match(Token.STAR, Token.SLASH):
            print(f"Info: parser: matched '{self.token.text}'")
            operator = self.token
            self.advance()
            right = self.unary()
            # expr = subtree.factor(expr, operator, right)

        return expr

    def unary(self):
        if self.token.match(Token.MINUS):
            print(f"Info: parser: matched '{self.token.text}'")
            operator = self.token
            self.advance()
            right = self.unary()

            # return subtree.unary(operator, right)
            return None

        return self.primary()

    def primary(self):
        if self.token.match(Token.LPAR):
            print(f"Info: parser: matched '{self.token.text}'")
            self.advance()

            # recurse back to the start symbol
            expr = self.expr()

            if self.token.match(Token.RPAR):
                print(f"Info: parser: matched '{self.token.text}'")
                self.advance()
            else:
                print(f"Error: parser: expect ')' after expression")
                exit(-1)

            # return subtree.grouping(expr)
            return None

        if self.token.match(Token.NUMBER):
            print(f"Info: parser: matched '{self.token.text}'")
            number = self.token
            self.advance()

            # return subtree.number(number)
            return None

        return None