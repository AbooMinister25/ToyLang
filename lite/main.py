from lark import Lark, Transformer


parser = Lark.open('lite\lite_parser.lark', parser="lalr", start="start")


class LiteTransformer(Transformer):
    def sum(self, args):
        return int(args[0]) + int(args[1])

    def sub(self, args):
        return int(args[0]) - int(args[1])

    def mul(self, args):
        return int(args[0]) * int(args[1])

    def div(self, args):
        return int(args[0]) / int(args[1])
    

if __name__ == '__main__':
    while True:
        data = input("> ")
        tree = parser.parse(data)
        print(LiteTransformer().transform(tree))
        
