from rply.token import BaseBox


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


class Newline():
    def eval(self):
        return "\n"


class String():
    def __init__(self, value):
        self.value = str(value).strip('"')

    def eval(self):
        return str(self.value)


class Sum():
    def __init__(self, value):
        self.value = value

    def eval(self, value):
        return sum(value)
