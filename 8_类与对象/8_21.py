# coding:utf-8

"""
实现访问者模式
"""


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, Node)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_number(self, node):
        return node.value

    def visit_add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_negate(self, node):
        return -node.operand


if __name__ == '__main__':
    pass
