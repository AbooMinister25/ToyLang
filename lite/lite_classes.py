class Environment():
    def __init__(self):
        self.variables = {}

    def get_variable(self, name):
        try:
            return self.variables[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")

    def assign_variable(self, name, value):
        if type(value) == str:
            value = value.strip('"')
        self.variables[name] = value


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return print(self.value)


class If():
    def __init__(self, left, right, expr, else_statement=False):
        self.left = left
        self.right = right
        self.expr = expr
        self.else_statement = else_statement

    def eval(self):
        if self.left == self.right:
            return self.expr
        else:
            return


class Input():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return input(self.value)
