from lark import Lark, Transformer, v_args
from lite_classes import Environment


@v_args(inline=True)    # Affects the signatures of the methods
class LiteTransformer(Transformer):
    number = int
    string = str

    def __init__(self):
        self.vars = {}

    def add(self, val1, val2):
        return int(val1) + int(val2)

    def sub(self, val1, val2):
        return int(val1) - int(val2)

    def mul(self, val1, val2):
        return int(val1) * int(val2)

    def div(self, val1, val2):
        return int(val1) / int(val2)

    def str_add(self, val1, val2):
        val1 = val1.strip('"')
        val2 = val2.strip('"')
        return str(val1) + str(val2)

    def print_statement(self, value=" "):
        if type(value) == str:
            value = value.strip('"')
        return value

    def input_statement(self, value):
        value = str(value).strip('"')
        input(value)

    def var_input_statement(self, name, value):
        name = input(value)
        self.assign_var(name, value)

    def get_var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")

    def assign_var(self, name, value):
        if name == "print":
            pass
        if type(value) == str:
            value = value.strip('"')
        self.vars[name] = value

    def true(self):
        return True

    def false(self):
        return False

    def expr_comparison(self, expr1, expr2):
        if expr1 == expr2:
            return True
        else:
            return False

    def if_statement(self, condition, *eval_expr):
        if condition:
            eval_expr
        else:
            return
    
    def if_statement(self, *value):
        return value
        
    def statement(self, *value):
        return value