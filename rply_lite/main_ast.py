from re import L
from rply.token import BaseBox
import random
import sys
import pdb


class Environment():
    def __init__(self):
        self.variables = {}

    def add_variable(self, name, value):
        self.variables.update({str(name): str(value)})

    def get_variable(self, variable):
        return self.variables[variable]


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.eval()


class Integer():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Input():
    def __init__(self, value):
        self.value = value

    def eval(self):
        input(self.value.eval())
        return


class Variable():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def eval(self):
        Environment().add_variable(self.name, self.value)
        print(Environment.get_variable(self, self.name))


class Newline():
    def __init__(self):
        pass

    def eval(self):
        return None


class String():
    def __init__(self, value):
        self.value = str(value).strip('"')

    def strip(self, value):
        self.value = self.value.strip(value)

    def eval(self):
        return str(self.value)


class Bool():
    def __init__(self, value):
        self.value = value

    def eval(self):
        if self.value == "false":
            return self.value
        if self.value == "true":
            return self.value
        else:
            return ValueError(f"Invalid value {self.value}")


class Null():

    def eval(self):
        return self

    def to_string(self):
        return 'null'


class Comparison():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        if self.left.eval() == self.right.eval():
            print("TRUE")
        else:
            print("FALSE")

    def if_eval(self):
        if self.left.eval() == self.right.eval():
            print("TRUE")
        else:
            print("FALSE")


class Block():
    def __init__(self, expression):
        self.expression = expression

    def eval(self):
        return self.expression.eval()


class If():
    def __init__(self, left, right, expr, else_statement=False):
        self.left = left
        self.right = right
        self.expr = expr
        self.else_statement = else_statement

    def eval(self):
        if self.left.eval() == self.right.eval():
            return self.expr.eval()
        else:
            if self.else_statement == False:
                return Bool("false")
            else:
                return self.else_statement.eval()


class Math():
    def __init__(self):
        pass

    def add(self, value):
        return sum(self.value)

    def random_int(self, range):
        return random.randint(range)

    def random_choice(self, values):
        return random.choice(values)
