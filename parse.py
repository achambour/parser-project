from lexer import Token
import syntaxtree
import pydot

class Syntax():
    def __init__(self, tokens):
        self.tokens = tokens
        self.graph = pydot.Dot(graph_type='graph')

    def expr(self):
        return self.term()

    def term(self):
        expr = self.factor()
        while self.tokens.match(Token.PLUS, Token.MINUS):
            operator = self.tokens.eat()
            right = self.factor()
            expr = syntaxtree.InfixExpr(expr, operator, right)
            self.graph.add_node(pydot.Node(id(operator), label=operator.text))
        return expr

    def factor(self):
        expr = self.unary()
        while self.tokens.match(Token.STAR, Token.SLASH):
            operator = self.tokens.eat()
            right = self.unary()
            expr = syntaxtree.InfixExpr(expr, operator, right)
            self.graph.add_node(pydot.Node(id(operator), label=operator.text))
        return expr

    def unary(self):
        if self.tokens.match(Token.MINUS):
            operator = self.tokens.eat()
            right = self.unary()
            expr = syntaxtree.UnaryExpr(operator, right)
            self.graph.add_node(pydot.Node(id(operator), label=operator.text))
            return expr
        return self.primary()

    def primary(self):
        if self.tokens.match(Token.LPAR):
            self.tokens.eat()
            expr = self.expr()
            if self.tokens.match(Token.RPAR):
                self.tokens.eat()
                return expr
            else:
                print("Parse error: expect ')' after expression")

        if self.tokens.match(Token.NUMBER):
            number = self.tokens.eat()
            expr = syntaxtree.NumberLiteral(number)
            self.graph.add_node(pydot.Node(id(number), label=number.text))
            return expr

        return None
