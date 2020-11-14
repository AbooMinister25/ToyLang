from lark import Lark
from lite_ast import *
from indenter import LiteIndenter
from lite_transformer import LiteTransformer


parser = Lark.open(os.path.join('lite', 'lite_parser.lark'),
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
