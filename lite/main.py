from lark import Lark, exceptions
from lite_ast import *
from lite_transformer import LiteTransformer
from lite_errors import *
import os
import sys


def get_correct_path(relative_path):
    try:
        base_path = sys.__MEIPASS
    except:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

parser = Lark.open("lite_parser.lark", rel_to = __file__,
                   parser='lalr')


def run_lite(filename=None):
    if filename == None:
        while True:
            lite_code = input("> ")
            try:
                tree = parser.parse(lite_code)
            except exceptions.UnexpectedToken as e:
                MissingToken(e.expected, e.line, e.column, e.get_context(lite_code))
                sys.exit()
            else:
                InvalidSyntax()
            try:
                x = LiteTransformer().transform(tree).eval(Env())
            except KeyError as e:
                InvalidName(e.args)
            except IndexError as e:
                InvalidIndex(e.args)
            except TypeError as e:
                InvalidType(e.args)
            else:
                InvalidSyntax()
    else:
        with open(filename, "r") as f:
            lite_code = f.read()
        try:
            tree = parser.parse(lite_code)
        except exceptions.UnexpectedToken as e:
            MissingToken(e.expected, e.line, e.column, e.get_context(lite_code))
            sys.exit()
        else:
            InvalidSyntax()
        try:
            x = LiteTransformer().transform(tree).eval(Env())
        except KeyError as e:
            InvalidName(e.args)
        except IndexError as e:
            InvalidIndex(e.args)
        except TypeError as e:
            InvalidType(e.args)
        else:
            InvalidSyntax()

def run_with_python_traceback(filename=None):
    if filename == None:
        while True:
            lite_code = input("> ")
            tree = parser.parse(lite_code)
            x = LiteTransformer().transform(tree).eval()
    else:
        with open(filename, "r") as f:
            lite_code = f.read()
            tree = parser.parse(lite_code)
            x = LiteTransformer().transform(tree).eval(Env())
        
        

if __name__ == '__main__':
    run_with_python_traceback('examples\python.lite')

