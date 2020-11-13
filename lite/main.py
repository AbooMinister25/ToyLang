from lark import Lark, Transformer, v_args
from transformer import LiteTransformer
from indenter import LiteIndenter

parser = Lark.open('lite\lite_parser.lark', parser='lalr')

if __name__ == '__main__':
    # while True:
    #     try:
    #         x = input("> ")
    #     except EOFError:
    #         break
    #     tree = parser.parse(x)
    #     print(LiteInterpreter().visit(tree))
    with open("test.lite", "r") as f:
        lite_code = f.read()

    tree = parser.parse(lite_code)
    print(LiteInterpreter().visit(tree))
