import random
import statistics
import os
import math
import sys
import time


class Env():
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.arg_functions = {}
        self.args = {}

    def get_variable(self, name):
        return self.variables[name]

    def assign_variable(self, name, value):
        self.variables[name] = value

    def define_function(self, name, eval_expr):
        self.functions[name] = eval_expr

    def assign_args(self, name, args):
        self.args[name] = args

    def define_args_function(self, name, eval_expr):
        self.arg_functions[name] = eval_expr

    def call_function(self, name):
        try:
            return self.functions[name].eval()
        except:
            raise Exception(f"Function {name} not found")

    def call_args_function(self, name, args):
        try:
            return self.args_functions[name].eval()(args)
        except:
            raise Exception(f"Function {name} not found")

    def get_array_index(self, name, index):
        return self.variables[name][int(index)]


environment = Env()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return print(self.value.eval())


class Input():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return input(self.value.eval())


class Add():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 + self.val2


class StringAdd():
    def __init__(self, val1, val2):
        self.val1 = str(val1)
        self.val2 = str(val2)

    def eval(self):
        return self.val1 + self.val2


class Sub():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 - self.val2


class Mul():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 * self.val2


class Div():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self):
        return self.val1 / self.val2


class String():
    def __init__(self, value):
        self.value = str(value).strip('"')

    def eval(self):
        return self.value


class Integer():
    def __init__(self, value):
        self.value = int(value)

    def eval(self):
        return self.value


class Array():
    def __init__(self, value):
        self.value = list(value)

    def eval(self):
        value = []
        for val in self.value:
            value.append(val.eval())
        return value


class AssignVariable():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        environment.assign_variable(self.name, self.value.eval())

    def __repr__(self):
        return f"Start({self.name}, {self.value})"


class GetVariable():
    def __init__(self, name, array=False):
        self.name = name
        self.array = array

    def eval(self):
        return environment.get_variable(self.name)

    def __repr__(self):
        return f"GetVaroab;e({self.name})"


class GetArrayIndex():
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def eval(self):
        return environment.get_array_index(self.name, self.index)


class Block():
    def __init__(self, exprs):
        self.exprs = exprs

    def eval(self):
        for expr in self.exprs:
            expr.eval()


class If():
    def __init__(self, expr1, expr2, eval_expr, else_statement=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr
        self.else_statement = else_statement

    def eval(self):
        if self.expr1.eval() == self.expr2.eval():
            self.eval_expr.eval()

        else:
            if self.else_statement == None:
                return
            else:
                self.else_statement.eval()

    def __repr__(self):
        return f"If({self.expr1}, {self.expr2}, {self.eval_expr}, {self.else_statement})"


class IfOr():
    def __init__(self, expr1, expr2, expr3, expr4, eval_expr, else_statement=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.expr4 = expr4
        self.else_statement = else_statement
        self.eval_expr = eval_expr

    def eval(self):
        if self.expr1.eval() == self.expr2.eval() or self.expr3.eval() == self.expr4.eval():
            self.eval_expr.eval()

        else:
            if self.else_statement == None:
                return
            else:
                self.else_statement.eval()


class AddVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self):
        if GetVariable(self.var1).eval() == String:
            var1 = str(GetVariable(self.var1).eval())
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var1).eval() == String:
            var2 = str(GetVariable(self.var2).eval())
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 + var2

    def __repr__(self):
        return f"AddVar({self.var1}, {self.var2})"


class Start():
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        for statement in self.statements:
            statement.eval()

    def __repr__(self):
        return f"Start({self.statements})"


class SubVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self):
        if GetVariable(self.var1).eval() == String:
            return ValueError("String object cannot be subtracted")
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var2).eval() == String:
            return ValueError("String object cannot be subtracted")
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 - var2

    def __repr__(self):
        return f"AddVar({self.var1}, {self.var2})"


class MulVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self):
        if GetVariable(self.var1).eval() == String:
            return ValueError("String object cannot be multiplied")
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var2).eval() == String:
            return ValueError("String object cannot be multiplied")
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 * var2


class DivVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self):
        if GetVariable(self.var1).eval() == String:
            return ValueError("String object cannot be divided")
        else:
            var1 = int(GetVariable(self.var1).eval())
        if GetVariable(self.var2).eval() == String:
            return ValueError("String object cannot be divided")
        else:
            var2 = int(GetVariable(self.var2).eval())
        return var1 / var2


class TrueBool():
    def __init__(self):
        self.value = True

    def eval(self):
        return self.value


class FalseBool():
    def __init__(self):
        self.value = False

    def eval(self):
        return self.value


class While():
    def __init__(self, condition, eval_expr):
        self.condition = condition
        self.eval_expr = eval_expr

    def eval(self):
        while self.condition.eval():
            self.eval_expr.eval()


class ConditionalLoop():
    def __init__(self, expr1, expr2, eval_expr):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr

    def eval(self):
        while self.expr1.eval() == self.expr2.eval():
            self.eval_expr.eval()


class Args():
    def __init__(self, args):
        self.args = args
        self.locals = {}

    def eval(self):
        return self.args


class InputArgs():
    def __init__(self, args):
        self.args = args
    
    def eval(self):
        return self.args.eval()


class ArgumentFunction():
    def __init__(self, name, args, eval_expr):
        self.name = name
        self.eval_expr = eval_expr
        self.args = args
        self.vars = {}

    def eval(self):
        environment.assign_args(self.name, self.args.eval())
        def myfunc():
            self.eval_expr.eval()
        environment.define_args_function(self.name, myfunc)


class CallArgumentFunction():
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
    def eval(self):
        environment.call_args_function(self.name, self.args.eval())


class Function():
    def __init__(self, name, eval_expr, args=None):
        self.name = name
        self.eval_expr = eval_expr
        self.args = args

    def eval(self):
        environment.define_function(self.name, self.eval_expr)


class CallFunction():
    def __init__(self, name):
        self.name = name

    def eval(self):
        environment.call_function(self.name)


class Sum():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return sum(self.value.eval())


class RandomInteger():
    def __init__(self, range1, range2):
        self.range1 = range1
        self.range2 = range2

    def eval(self):
        return random.randint(self.range1.eval(), self.range2.eval())


class ReadFile():
    def __init__(self, filename):
        self.filename = filename

    def eval(self):
        data = open(self.filename.eval(), "r")
        return data.readlines()


class Doc():
    def __init__(self, value):
        self.value = value
        self.docstrings = {
            "print": "print: statement for outputing data to the console",
            "input": "input: statement for gathering user input through the console",
            "string": "string data type",
            "integer": "integer data type",
            "array": "array data type, can have both string and integer values",
            "if": "if: statement for comparing two values",
            "else": "else: else statement block is evaluated when preceding if statement returns false",
            "while": "while: statement for defining while loops.",
            "function": "function: statement for defining a function",
            "true": "true: boolean data type",
            "false": "false: boolean data type",
            "sum": "sum: expression for getting the combined sum for all the values in an array",
            "random_integer": "random_integer: expression for getting a random integer from between two given ranges",
            "read_file": "expression: expression for reading the data from a file",
            "mean": "expression: expression for returning the mean of a given data set",
            "square_root": "expression for returning the square_root of an integer",
            "exit": "statement: statement for exiting the program, can have an optional exit message"
        }

    def eval(self):
        try:
            return self.docstrings[self.value.eval()]
        except:
            return Exception(f"Docstring for {self.value} not found")


class Mean():
    def __init__(self, data):
        self.data = data

    def eval(self):
        return statistics.mean(self.data.eval())


class SquareRoot():
    def __init__(self, data):
        self.data = data

    def eval(self):
        return math.sqrt(self.data.eval())


class Exit():
    def __init__(self, message):
        self.message = message

    def eval(self):
        sys.exit(self.message.eval())


class PathExists():
    def __init__(self, path):
        self.path = path

    def eval(self):
        return os.path.exists(self.path.eval())


class Wait():
    def __init__(self, time):
        self.time = time

    def eval(self):
        return time.sleep(self.time.eval())
