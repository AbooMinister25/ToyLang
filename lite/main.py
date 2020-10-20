from lexer import Lexer
from main_parser import Parser

pg = Parser()
pg.parse()

lexer = Lexer()

parser = pg.build_parser()

with open('test.lite', 'r') as f:
    lines = f.readlines()

if __name__ == '__main__':
    for line in lines:
        if line == "\n":
            continue
        result = parser.parse(lexer.lex(line)).eval()
        print(result)

