from lark import Lark, Transformer, v_args
from lite_classes import *
from lark.visitors import Interpreter


@v_args(inline=True) 
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

    def if_statement(self, condition, *eval_expr):
        if condition == True:
            for expr in eval_expr:
                return expr
        else:
            return

    def if_statements(self, *value):
        return

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

    def var_input_statement(self, name, value):
        data = self.input_statement(value, store_data=True)
        self.assign_var(name, data)

    def input_statement(self, value=" ", store_data=False):
        if type(value) == str:
            value = value.strip('"')
        if store_data == True:
            data = input(value)
            return data
        else:
            return Input(value)

    def print_statement(self, value=" "):
        if type(value) == str:
            value = value.strip('"')
        return Print(value)

    def expr_comparison(self, expr1, expr2):
        if expr1 == expr2:
            return print("HI")
        else:
            return False

    def statement(self, *values):
        for value in values:
            if value == None:
                pass
            else:
                value.eval()
