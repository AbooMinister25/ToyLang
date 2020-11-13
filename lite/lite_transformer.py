from lark import Lark, Transformer, v_args
from lite_ast import *
from indenter import LiteIndenter


@v_args(inline=True)
class LiteTransformer(Transformer):
    def __init__(self):
        ...

    def number(self, value):
        return Integer(value)

    def string(self, value):
        value = str(value).strip('"')
        return String(value)

    def add(self, val1, val2):
        return Add(val1, val2)

    def sub(self, val1, val2):
        return Sub(val1, val2)

    def mul(self, val1, val2):
        return Mul(val1, val2)

    def div(self, val1, val2):
        return Div(val1, val2)

    def str_add(self, val1, val2):
        return StringAdd(val1, val2)

    def print_statement(self, value):
        return Print(value)

    def input_statement(self, value):
        return Input(value)

    def var_input_statement(self, name, value):
        return AssignVariable(name, Input(value))

    def assign_var(self, name, value):
        return AssignVariable(name, value)

    def get_var(self, name):
        return GetVariable(name)

    def var_add(self, var1, var2):
        return AddVar(var1, var2)

    def expr_comparison(self, expr1, expr2):
        return Comparison(expr1, expr2)

    def if_statement(self, expr1, expr2, *eval_expr):
        return If(expr1, expr2, eval_expr)

    def if_else_statement(self, expr1, expr2, eval_expr, else_statement):
        return If(expr1, expr2, eval_expr, else_statement)

    # def statement(self, *values):
    #     for value in values:
    #         value.eval()


parser = Lark.open('lite\lite_parser.lark',
                   parser='lalr', postlex=LiteIndenter())

if __name__ == '__main__':
    # while True:
    #     try:
    #         x = input("> ")
    #     except EOFError:
    #         break
    #     tree = parser.parse(x)
    #     print(LiteTransformer().transform(tree))
    with open("test.lite", "r") as f:
        lite_code = f.read()

    tree = parser.parse(lite_code)
    x = LiteTransformer().transform(tree)
    x.eval()
