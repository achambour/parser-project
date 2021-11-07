class TreeNode():
    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right


class InfixExpr(TreeNode):
    def __init__(self, left, operator, right):
        super().__init__(left, operator, right)


class UnaryExpr(TreeNode):
    def __init__(self, operator, expr):
        super().__init__(expr, operator, None)


class NumberLiteral(TreeNode):
    def __init__(self, number):
        super().__init__(None, number, None)
