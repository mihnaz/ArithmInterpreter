import math


class NumberExpression:
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


class SumExpression:
    def __init__(self, expression1, expression2):
        self.child_expression1 = expression1
        self.child_expression2 = expression2

    def interpret(self):
        return self.child_expression1.interpret() + self.child_expression2.interpret()


class MulExpression:
    def __init__(self, expression1, expression2):
        self.child_expression1 = expression1
        self.child_expression2 = expression2

    def interpret(self):
        return self.child_expression1.interpret() * self.child_expression2.interpret()


class DivExpression:
    def __init__(self, expression1, expression2):
        self.child_expression1 = expression1
        self.child_expression2 = expression2

    def interpret(self):
        return self.child_expression1.interpret() / self.child_expression2.interpret()


class SubExpression:
    def __init__(self, expression1, expression2):
        self.child_expression1 = expression1
        self.child_expression2 = expression2

    def interpret(self):
        return self.child_expression1.interpret() - self.child_expression2.interpret()


class SinExpression:
    def __init__(self, expression1):
        self.child_expression1 = expression1

    def interpret(self):
        return math.sin(self.child_expression1.interpret())


class BigEqExpression:
    def __init__(self, expression1, expression2):
        self.child_expression1 = expression1
        self.child_expression2 = expression2

    def interpret(self):
        return self.child_expression1.interpret() >= self.child_expression2.interpret()
