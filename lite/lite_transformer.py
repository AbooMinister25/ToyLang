from lark import Lark, Transformer, v_args
from lite_ast import *
from lite_errors import *
from lark import exceptions
import os.path
import sys


@v_args(inline=True)
class LiteTransformer(Transformer):
    def __init__(self):
        ...

    def number(self, value):
        return Integer(value)

    def string(self, value):
        value = str(value).strip('"')
        return String(value)

    def array(self, *value):
        return Array(value)

    def add(self, val1, val2):
        return Add(val1, val2)

    def sub(self, val1, val2):
        return Sub(val1, val2)

    def mul(self, val1, val2):
        return Mul(val1, val2)

    def div(self, val1, val2):
        return Div(val1, val2)

    def str_add(self, val1, val2):
        return StringAdd(val1, val2)

    def var_add(self, var1, var2):
        return AddVar(var1, var2)

    def var_sub(self, var1, var2):
        return SubVar(var1, var2)

    def var_mul(self, var1, var2):
        return MulVar(var1, var2)

    def var_div(self, var1, var2):
        return DivVar(var1, var2)

    def true(self):
        return TrueBool()

    def false(self):
        return FalseBool()

    def sum_expr(self, value):
        return Sum(value)

    def random_integer(self, range1, range2):
        return RandomInteger(range1, range2)

    def read_file(self, filename):
        return ReadFile(filename)

    def doc(self, value):
        return Doc(value)

    def print_statement(self, value, semicolon):
        return Print(value)

    def input_statement(self, value):
        return Input(value)

    def var_input_statement(self, name, value):
        return AssignVariable(name, value=Input(value))

    def assign_var(self, name, value):
        return AssignVariable(name, value)

    def get_var(self, name):
        return GetVariable(name)
    
    def array_index(self, name, index):
        return GetArrayIndex(name, index)
    
    def mean(self, value):
        return Mean(value)
    
    def square_root(self, value):
        return SquareRoot(value)
    
    def exit_statement(self, message=None):
        return Exit(message)
    
    def path_exists(self, path):
        return PathExists(path)

    def expr_comparison(self, expr1, expr2):
        return Comparison(expr1, expr2)

    def if_statement(self, expr1, expr2, eval_expr):
        return If(expr1, expr2, eval_expr)

    def if_else_statement(self, expr1, expr2, eval_expr, else_statement):
        return If(expr1, expr2, eval_expr, else_statement)
    
    def or_if_statement(self, expr1, expr2, expr3, expr4, eval_expr):
        return IfOr(expr1, expr2, expr3, expr4, eval_expr)

    def while_loop(self, condition, eval_expr):
        return While(condition, eval_expr)

    def conditional_loop(self, expr1, expr2, eval_expr):
        return ConditionalLoop(expr1, expr2, eval_expr)

    def no_argument_function(self, name, eval_expr):
        return Function(name, eval_expr)

    def no_argument_call_function(self, name):
        return CallFunction(name)
    
    def wait(self, time):
        return Wait(time)

    def block(self, *exprs):
        return Block(exprs)
    
    def args(self, *arguments):
        return Args(arguments)

    def COMMENT(self):
        pass

    def start(self, *statements):
        return Start(statements)

if __name__ == '__main__':
    # while True:
    #     try:
    #         x = input("> ")
    #     except EOFError:
    #         break
    #     tree = parser.parse(x)
    #     print(LiteTransformer().transform(tree))
    with open("test.lite", "r") as f:
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

