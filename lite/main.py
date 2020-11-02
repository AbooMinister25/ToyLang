from lark import Lark, Transformer, v_args
from transformer import LiteTransformer
from indenter import LiteIndenter


parser = Lark.open('lite\lite_parser.lark', parser="lalr",
                   transformer=LiteTransformer(), postlex=LiteIndenter())
lite_parser = parser.parse


if __name__ == '__main__':
    # while True:
    #     try:
    #         x = input("> ")
    #     except EOFError:
    #         break
    #     print(lite_parser(x))
    with open("test.lite", "r") as f:
        lite_code = f.read()
    
    print(lite_parser(lite_code))
