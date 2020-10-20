from rply import ParserGenerator
from ast import *
from errors import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['PRINT', 'INTEGER', 'STRING', "LPAREN", 'RPAREN', 'PLUS',
                'MINUS', 'MUL', 'DIV', 'INPUT', 'SEMICOLON', 'NEWLINE', "VARIABLE", "EQUALS", "STRING", '$end'],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV'])
            ]
        )

    def parse(self):
        @self.pg.production('expression : PRINT LPAREN expression RPAREN SEMICOLON')
        def print_obj(p):
            return Print(p[2])

        @self.pg.production('expression : INPUT LPAREN expression RPAREN SEMICOLON')
        def input(p):
            return Input(p[2])

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'PLUS':
                return Add(left, right)
            elif p[1].gettokentype() == 'MINUS':
                return Sub(left, right)
            elif p[1].gettokentype() == 'MUL':
                return Mul(left, right)
            elif p[1].gettokentype() == 'DIV':
                return Div(left, right)
            else:
                raise AssertionError(f'Invalid operator {p[1].gettokentype()}')

        @self.pg.production('expression : INTEGER')
        def integer(p):
            return Integer(int(p[0].getstr()))

        @self.pg.production('expression : STRING')
        def string(p):
            return String(str(p[0].getstr()))

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Invalid token {token}")

    def build_parser(self):
        return self.pg.build()
