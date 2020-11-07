class Environment():
    def __init__(self):
        self.vars = {}

    def get_variable(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")

    def assign_variable(self, name, value):
        if type(value) == str:
            value = value.strip('"')
        self.vars[name] = value


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


class AssignVar(Environment):
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def eval(self):
        self.assign_variable(self.name, self.value)


class GetVar(Environment):
    def __init__(self, name):
        self.var = name

    def eval(self):
        self.get_variable(self.var)
