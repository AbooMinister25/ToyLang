from lark import Lark, Transformer


parser = Lark.open('lite\lite_parser.lark', parser="lalr", start="value")


class LiteTransformer(Transformer):
    def add(self, args):
        return int(args[0]) + int(args[1])

    def sub(self, args):
        return int(args[0]) - int(args[1])

    def mul(self, args):
        return int(args[0]) * int(args[1])

    def div(self, args):
        return int(args[0]) / int(args[1])
    
    def print(self, args):
        print(args)
        
    def input(self, args):
        input(args)


if __name__ == '__main__':
    while True:
        data = input("> ")
        tree = parser.parse(data)
        print(LiteTransformer().transform(tree))
        
