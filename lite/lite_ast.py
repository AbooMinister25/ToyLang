class Env():
    def __init__(self):
        self.variables = {}

    def get_variable(self, name):
        try:
            return self.variables[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")

    def assign_variable(self, name, value):
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


class StringAdd():
    def __init__(self, val1, val2):
        self.val1 = str(val1)
        self.val2 = str(val2)
    
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
        return environment.get_variable(self.name).eval()


class Comparison():
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def eval(self):
        if self.expr1.eval() == self.expr2.eval():
            return True
        else:
            return

class If():
    def __init__(self, expr1, expr2, eval_expr, else_statement=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr
        self.else_statement = else_statement
        
    def eval(self):
        if self.expr1.eval() == self.expr2.eval():
            return self.eval_expr.eval()
        else:
            if self.else_statement == None:
                return
            else:
                return self.else_statement.eval()

class AddVar():
    def __init__(self, var1, var2):
        self.var1 = environment.get_variable(var1).eval()
        self.var2 = environment.get_variable(var2).eval()
    
    def eval(self):
        return self.var1 + self.var2