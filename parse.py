from lexer import Token
import tree


class Syntax():
    def __init__(self, tokens):
        self.tokens = tokens

    def expr(self):
        self.term()

    def term(self):
        left = self.factor()
        while self.tokens.match(Token.PLUS, Token.MINUS):
            operator = self.tokens.eat()
            right = self.factor()
            expr = tree.InfixExpr(left, operator, right)
        return expr

    def factor(self):
        left = self.unary()
        while self.tokens.match(Token.STAR, Token.SLASH):
            operator = self.tokens.eat()
            right = self.unary()
            expr = tree.InfixExpr(left, operator, right)
        return expr

    def unary(self):
        if self.tokens.match(Token.MINUS):
            operator = self.tokens.eat()
            right = self.unary()
            return tree.UnaryExpr(operator, right)
        return self.primary()

    def primary(self):

        if self.tokens.match(Token.LPAR):
            self.tokens.eat()
            expr = self.expr()
            if self.tokens.match(Token.RPAR):
                self.tokens.eat()
                return tree.NestedGroup(expr)
            else:
                print("Parse error: expect ')' after expression")

        if self.tokens.match(Token.NUMBER):
            number = self.tokens.eat()
            return tree.NumberLiteral(number)

        return None