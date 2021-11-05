from lexer import Token


class Syntax():
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
