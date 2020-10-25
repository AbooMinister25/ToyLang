from rply import ParserGenerator
from ast import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['PRINT', 'IF', 'INTEGER', 'STRING', "LPAREN", 'RPAREN', 'PLUS',
                'MINUS', 'MUL', 'DIV', 'INPUT', 'SEMICOLON', 'NEWLINE', "EQUALS", "STRING", "ELSE", "COMPARISON", "SUM", "RANDOM_INT", "RBRACKET", "LBRACKET", '$end'],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
                ('left', ['COMPARISON']),
                ('left', ['IF'])
            ]
        )

    def parse(self):
        @self.pg.production('expression : PRINT LPAREN expression RPAREN SEMICOLON')
        def print_obj(p):
            return Print(p[2])

        @self.pg.production('expression : INPUT LPAREN expression RPAREN SEMICOLON')
        def input(p):
            return Input(p[2])
        
        @self.pg.production('block : expression')
        def block(p):
            return Block(p[0])

        @self.pg.production('expression : IF expression COMPARISON expression LBRACKET NEWLINE expression NEWLINE RBRACKET')
        def if_statement(p):
            return If(p[1], p[3], p[6])

        @self.pg.production('expression : IF expression COMPARISON expression LBRACKET expression RBRACKET')
        def single_line_if_statement(p):
            return If(p[1], p[3], p[5])

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression COMPARISON expression')
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
            elif p[1].gettokentype() == 'COMPARISON':
                print(left, right)
                return Comparison(left, right)
            else:
                raise AssertionError(f'Invalid operator {p[1].gettokentype()}')

        @self.pg.production('expression : INTEGER')
        def integer(p):
            return Integer(int(p[0].getstr()))
        
        @self.pg.production('expression : NEWLINE')
        def newline(p):
            pass

        @self.pg.production('expression : STRING')
        def string(p):
            return String(str(p[0].getstr()))

        @self.pg.production('expression : RANDOM_INT LPAREN expression RPAREN')
        def random_str(p):
            return random_int(int[p[2]], int[[[3]]])

        @self.pg.production('expression : SUM LPAREN expression RPAREN')
        def sum(p):
            return sum(int[p[2]])

        @self.pg.error
        def error_handle(token):
            raise ValueError(f"Invalid token {token} {token.value} at {token.getsourcepos()}")

    def build_parser(self):
        return self.pg.build()
