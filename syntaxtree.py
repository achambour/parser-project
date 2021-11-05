class TreeNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Infix(TreeNode):
    def __init__(self, left, operator, right):
        super().__init__(left, right)
        print(left, operator.text, right)


class Unary(TreeNode):
    def __init__(self, operator, expr):
        super().__init__(expr, None)
        print(operator.text, expr)


class NumberLiteral(TreeNode):
    def __init__(self, number):
        super().__init__(None, None)
