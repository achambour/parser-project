from lexer import Token
import syntaxtree


class Syntax():
    def __init__(self, tokens):
        self.tokens = tokens

    def expr(self):
        self.term()

    def term(self):
        expr = self.factor()
        while self.tokens.match(Token.PLUS, Token.MINUS):
            operator = self.tokens.eat()
            right = self.factor()
            expr = syntaxtree.Infix(expr, operator, right)
        return expr

    def factor(self):
        expr = self.unary()
        while self.tokens.match(Token.STAR, Token.SLASH):
            operator = self.tokens.eat()
            right = self.unary()
            expr = syntaxtree.Infix(expr, operator, right)
        return expr

    def unary(self):
        if self.tokens.match(Token.MINUS):
            operator = self.tokens.eat()
            right = self.unary()
            return syntaxtree.Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.tokens.match(Token.LPAR):
            self.tokens.eat()
            expr = self.expr()
            if self.tokens.match(Token.RPAR):
                self.tokens.eat()
                return syntaxtree.NestedGroup(expr)
            else:
                print("Parse error: expect ')' after expression")

        if self.tokens.match(Token.NUMBER):
            number = self.tokens.eat()
            return syntaxtree.NumberLiteral(number)

        return None