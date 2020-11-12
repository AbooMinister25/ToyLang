from lark import Lark, Transformer, v_args
from lite_ast import *
from lark.visitors import Interpreter
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
    
    def print_statement(self, value):
        return Print(value).eval()
    
    def input_statement(self, value):
        return Input(value).eval()
    
    def assign_var(self, name, value):
        return AssignVariable(name, value)
    
    def get_var(self, name):
        return GetVariable(name)


parser = Lark.open('lite\lite_parser.lark',
                   parser='lalr', postlex=LiteIndenter())

if __name__ == '__main__':
    # while True:
    #     try:
    #         x = input("> ")
    #     except EOFError:
    #         break
    # print(lite_parser(x))
    with open("test.lite", "r") as f:
        lite_code = f.read()
    
    tree = parser.parse(lite_code)
    print(LiteTransformer().transform(tree))

