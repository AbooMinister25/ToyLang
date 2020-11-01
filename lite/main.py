from lark import Lark, Transformer, v_args


@v_args(inline=True)    # Affects the signatures of the methods
class LiteTransformer(Transformer):
    number = int

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

    def print_statement(self, value):
        value = str(value).strip('"')
        return value

    def input_statement(self, value):
        value = str(value).strip('"')
        input(value)


parser = Lark.open('lite\lite_parser.lark', parser="lalr",
                   transformer=LiteTransformer())
lite_parser = parser.parse


if __name__ == '__main__':
    while True:
        try:
            x = input("> ")
        except EOFError:
            break
        print(lite_parser(x))
