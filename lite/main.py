from lark import Lark, exceptions
from lite_ast import *
from lite_transformer import LiteTransformer
from lite_errors import *
import os
import sys


def get_correct_path(relative_path):
    try:
        base_path = sys.__MAIPASS
    except:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

try:
    parser = Lark.open(get_correct_path("lite\lite_parser.lark"),
                   parser='lalr')
except:
    parser = Lark.open('lite\lite_parser.lark', parser='lalr')

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
                x = LiteTransformer().transform(tree).eval()
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
            x = LiteTransformer().transform(tree).eval()
        except KeyError as e:
            InvalidName(e.args)
        except IndexError as e:
            InvalidIndex(e.args)
        except TypeError as e:
            InvalidType(e.args)
        else:
            InvalidSyntax()

if __name__ == '__main__':
    run_lite()
