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
        environment.assign_variable(self.name, self.value.eval())

    def __repr__(self):
        return f"Start({self.name}, {self.value})"


class GetVariable():
    def __init__(self, name):
        self.name = name

    def eval(self):
        return environment.get_variable(self.name)

    def __repr__(self):
        return f"GetVaroab;e({self.name})"


class If():
    def __init__(self, expr1, expr2, eval_expr, else_statement=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr
        self.else_statement = else_statement

    def eval(self):
        if self.expr1.eval() == self.expr2.eval():
            for expr in self.eval_expr:
                expr.eval()
        else:
            if self.else_statement == None:
                return
            else:
                for expr in self.else_statement:
                    expr.eval()

    def __repr__(self):
        return f"If({self.expr1}, {self.expr2}, {self.eval_expr}, {self.else_statement})"


class AddVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self):
        if GetVariable(self.var1).eval() == String:
            var1 = str(GetVariable(self.var1).eval())
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var1).eval() == String:
            var2 = str(GetVariable(self.var2).eval())
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 + var2
    
    def __repr__(self):
        return f"AddVar({self.var1}, {self.var2})"

class Start():
    def __init__(self, statements):
        self.statements = statements
    
    def eval(self):
        for statement in self.statements:
            statement.eval()
    
    def __repr__(self):
        return f"Start({self.statements})"

class SubVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self):
        if GetVariable(self.var1).eval() == String:
            return ValueError("String object cannot be subtracted")
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var2).eval() == String:
            return ValueError("String object cannot be subtracted")
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 - var2
    
    def __repr__(self):
        return f"AddVar({self.var1}, {self.var2})"

class MulVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def eval(self):
        if GetVariable(self.var1).eval() == String:
            return ValueError("String object cannot be multiplied")
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var2).eval() == String:
            return ValueError("String object cannot be multiplied")
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 * var2

class DivVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def eval(self):
        if GetVariable(self.var1).eval() == String:
            return ValueError("String object cannot be divided")
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var2).eval() == String:
            return ValueError("String object cannot be divided")
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 / var2