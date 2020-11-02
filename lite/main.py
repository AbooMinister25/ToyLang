from lark import Lark, Transformer, v_args
from transformer import LiteTransformer


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
