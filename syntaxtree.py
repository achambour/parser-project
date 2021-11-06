class TreeNode():
    def __init__(self, token, left, right):
        self.token = token
        self.left = left
        self.right = right


class InfixExpr(TreeNode):
    def __init__(self, left, operator, right):
        super().__init__(operator, left, right)


class UnaryExpr(TreeNode):
    def __init__(self, operator, expr):
        super().__init__(operator, expr, None)


class NumberLiteral(TreeNode):
    def __init__(self, number):
        super().__init__(number, None, None)
