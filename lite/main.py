from lexer import Lexer
from main_parser import Parser

pg = Parser()
pg.parse()

lexer = Lexer()

parser = pg.build_parser()

with open('test.lite', 'r') as f:
    code = f.read()
    lines = f.readlines()
    
if __name__ == '__main__':
    tokens = lexer.lex(code)
    print(parser.parse(tokens).eval())
