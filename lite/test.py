from lark import Lark, Transformer


parser = Lark("""
start: add
     | sub
     | mul
     | div

add: NUMBER "+" NUMBER
sub: NUMBER "-" NUMBER
mul: NUMBER "*" NUMBER
div: NUMBER "/" NUMBER


%import common.NUMBER
%ignore " "

    """, start="start")


class CalcTransformer(Transformer):
    def add(self, args):
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
        print(CalcTransformer().transform(tree))
