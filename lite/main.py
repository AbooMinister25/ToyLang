from lark import Lark, Transformer, v_args

@v_args(inline=True)
class LiteTransformer(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float
    
    def __init__(self):
        self.vars = {}
    
    def assign_var(self, name, value):
        self.vars[name] = value
    
    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")
    
    # def print(self, value):
    #     print(value)
        

parser = Lark.open('lite\lite_parser.lark', parser="lalr", start="start")


if __name__ == '__main__':
    while True:
        try:
            x = input("> ")
            tree = parser.parse(x)
            print(LiteTransformer().transform(tree))
        except EOFError:
            break
