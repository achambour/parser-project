class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None


class Infix(TreeNode):
    def __init__(self, left, operator, right):
        super().__init__()
        print(f"InfixExpr: {left, operator, right}")


class Unary(TreeNode):
    def __init__(self, operator, right):
        super().__init__()
        print(f"UnaryExpr: {operator, right}")


class NestedGroup(TreeNode):
    def __init__(self, expr):
        super().__init__()
        print(f"NestedGroup: {expr}")


class NumberLiteral(TreeNode):
    def __init__(self, number):
        super().__init__()