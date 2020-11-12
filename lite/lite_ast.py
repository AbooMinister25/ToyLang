class Env():
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

environment = Env()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return print(self.value.eval())


class Input():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return input(self.value.eval())


class Add():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 + self.val2


class Sub():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 - self.val2


class Mul():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 * self.val2


class Div():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 / self.val2


class String():
    def __init__(self, value):
        self.value = str(value).strip('"')

    def eval(self):
        return self.value


class Integer():
    def __init__(self, value):
        self.value = int(value)

    def eval(self):
        return self.value

class AssignVariable():
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def eval(self):
        environment.assign_variable(self.name, self.value)


class GetVariable():
    def __init__(self, name):
        self.name = name
    
    def eval(self):
        return environment.variables[self.name]
