"""
Lexer
"""

from rply import LexerGenerator
import re


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('STRING', '(""".*?""")|(".*?")|(\'.*?\')')
        self.lexer.add("INTEGER", r'\d+')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')
        self.lexer.add('PRINT', r"print")
        self.lexer.add("INPUT", r'input')
        self.lexer.add("SEMICOLON", r'\;')
        self.lexer.add("NEWLINE", r"\n")
        self.lexer.add("VARIABLE", "[a-zA-Z_][a-zA-Z0-9_]")
        self.lexer.add("EQUALS", r'=')
        self.lexer.add("SUM", r"sum")

        self.lexer.ignore('[ \t\r\f\v]+')
        self.lexer.ignore("\n")

    def lex(self, source):
        self._add_tokens()
        lexer = self.lexer.build()
        return lexer.lex(source)
