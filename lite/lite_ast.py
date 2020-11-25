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

    def define_function(self, name, eval_expr, args):
        self.functions[name] = {"eval": eval_expr, "args": args}

    def assign_args(self, name, args):
        self.args[name] = args

    def define_args_function(self, name, eval_expr):
        self.arg_functions[name] = eval_expr

    def call_function(self, name, args):
        try:
            len_args = len(self.functions[name]["args"].eval(self))
            if args is None:
                pass
            else:
                if len_args == len(args):
                    eval_args = [arg.eval(self) for arg in args]
                    for arg in eval_args:
                        self.functions[name]["eval"].local.assign_variable(self.functions[name]["args"].eval(self)[eval_args.index(arg)], arg)
                else:
                    return Exception("Invalid Number Of Arguments Given")
        except Exception as e:
            raise e
        return self.functions[name]["eval"].eval(self)

    def call_args_function(self, name, args):
        try:
            return self.arg_functions[name](args)
        except:
            raise Exception(f"Function {name} not found")

    def get_array_index(self, name, index):
        return self.variables[name][int(index)]


environment = Env()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return print(self.value.eval(env))


class Input():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return input(self.value.eval(env))


class Add():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self, env):
        return self.val1 + self.val2


class StringAdd():
    def __init__(self, val1, val2):
        self.val1 = str(val1)
        self.val2 = str(val2)

    def eval(self, env):
        return self.val1 + self.val2


class Sub():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self, env):
        return self.val1 - self.val2


class Mul():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self, env):
        return self.val1 * self.val2


class Div():
    def __init__(self, val1, val2):
        self.val1 = int(val1)
        self.val2 = int(val2)

    def eval(self, env):
        return self.val1 / self.val2


class String():
    def __init__(self, value):
        self.value = str(value).strip('"')

    def eval(self, env):
        return self.value


class Integer():
    def __init__(self, value):
        self.value = int(value)

    def eval(self, env):
        return self.value


class Array():
    def __init__(self, value):
        self.value = list(value)

    def eval(self, env):
        value = []
        for val in self.value:
            value.append(val.eval(env))
        return value


class AssignVariable():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self, env):
        env.assign_variable(self.name, self.value.eval(env))

    def __repr__(self):
        return f"Start({self.name}, {self.value})"


class GetVariable():
    def __init__(self, name, array=False):
        self.name = name
        self.array = array

    def eval(self, env):
        return env.get_variable(self.name)

    def __repr__(self):
        return f"GetVariblee({self.name})"


class GetArrayIndex():
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def eval(self, env):
        return env.get_array_index(self.name, self.index)


class Block():
    def __init__(self, exprs):
        self.exprs = exprs

    def eval(self, env):
        for expr in self.exprs:
            expr.eval(env)


class If():
    def __init__(self, expr1, expr2, eval_expr, else_statement=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr
        self.else_statement = else_statement

    def eval(self, env):
        if self.expr1.eval(env) == self.expr2.eval(env):
            self.eval_expr.eval(env)

        else:
            if self.else_statement == None:
                return
            else:
                self.else_statement.eval(env)

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

    def eval(self, env):
        if self.expr1.eval(env) == self.expr2.eval(env) or self.expr3.eval(env) == self.expr4.eval(env):
            self.eval_expr.eval(env)

        else:
            if self.else_statement == None:
                return
            else:
                self.else_statement.eval(env)


class AddVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self, env):
        if GetVariable(self.var1).eval(env) == String:
            var1 = str(GetVariable(self.var1).eval(env))
        else:
            var1 = int(GetVariable(self.var1).eval(env))
        if GetVariable(self.var1).eval(env) == String:
            var2 = str(GetVariable(self.var2).eval(env))
        else:
            var2 = int(GetVariable(self.var2).eval(env))
        return var1 + var2

    def __repr__(self):
        return f"AddVar({self.var1}, {self.var2})"


class Start():
    def __init__(self, statements):
        self.statements = statements

    def eval(self, env):
        for statement in self.statements:
            statement.eval(env)

    def __repr__(self):
        return f"Start({self.statements})"


class SubVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self, env):
        if GetVariable(self.var1).eval(env) == String:
            return ValueError("String object cannot be subtracted")
        else:
            var1 = int(GetVariable(self.var1).eval(env))
        if GetVariable(self.var2).eval(env) == String:
            return ValueError("String object cannot be subtracted")
        else:
            var2 = int(GetVariable(self.var2).eval(env))
        return var1 - var2

    def __repr__(self):
        return f"AddVar({self.var1}, {self.var2})"


class MulVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self, env):
        if GetVariable(self.var1).eval(env) == String:
            return ValueError("String object cannot be multiplied")
        else:
            var1 = int(GetVariable(self.var1).eval(env))
        if GetVariable(self.var2).eval(env) == String:
            return ValueError("String object cannot be multiplied")
        else:
            var2 = int(GetVariable(self.var2).eval(env))
        return var1 * var2


class DivVar():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def eval(self, env):
        if GetVariable(self.var1).eval(env) == String:
            return ValueError("String object cannot be divided")
        else:
            var1 = int(GetVariable(self.var1).eval(env))
        if GetVariable(self.var2).eval(env) == String:
            return ValueError("String object cannot be divided")
        else:
            var2 = int(GetVariable(self.var2).eval(env))
        return var1 / var2


class TrueBool():
    def __init__(self):
        self.value = True

    def eval(self, env):
        return self.value


class FalseBool():
    def __init__(self):
        self.value = False

    def eval(self, env):
        return self.value


class While():
    def __init__(self, condition, eval_expr):
        self.condition = condition
        self.eval_expr = eval_expr

    def eval(self, env):
        while self.condition.eval(env):
            self.eval_expr.eval(env)


class ConditionalLoop():
    def __init__(self, expr1, expr2, eval_expr):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr

    def eval(self, env):
        while self.expr1.eval(env) == self.expr2.eval(env):
            self.eval_expr.eval(env)


class FuncBlock():
    def __init__(self, exprs):
        self.exprs = exprs
        class Local():
            def __init__(self):
                self.functions = {}
                self.variables = {}
            
            def get_variable(self, name):
                return self.variables[name]
            
            def assign_variable(self, name, value):
                self.variables[name] = value
            
            def define_function(self, name, eval_expr, args):
                self.functions[name] = {"eval": eval_expr, "args": args}
            
            def call_funciton(self, name):
                args = self.functions[name]["args"]
                if args is None:
                    pass
                else:
                    eval_args = [arg.eval(self) for arg in args]
                return self.functions[name]["eval"].eval(self)

            def get_array_index(self, name, index):
                return self.variables[name][int(index)]
        
        self.local = Local()

    def eval(self, env):
        for expr in self.exprs:
            expr.eval(self.local)


class Args():
    def __init__(self, args):
        self.args = args
        self.locals = {}

    def eval(self, env):
        return self.args

class Function():
    def __init__(self, name, eval_expr, args=None):
        self.name = name
        self.eval_expr = eval_expr
        self.args = args

    def eval(self, env):
        env.define_function(self.name, self.eval_expr, self.args)


class CallFunction():
    def __init__(self, name, args=None):
        self.name = name
        self.args = args

    def eval(self, env):
        env.call_function(self.name, self.args)


class Sum():
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return sum(self.value.eval(env))


class RandomInteger():
    def __init__(self, range1, range2):
        self.range1 = range1
        self.range2 = range2

    def eval(self, env):
        return random.randint(self.range1.eval(env), self.range2.eval(env))


class ReadFile():
    def __init__(self, filename):
        self.filename = filename

    def eval(self, env):
        data = open(self.filename.eval(env), "r")
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

    def eval(self, env):
        try:
            return self.docstrings[self.value.eval(env)]
        except:
            return Exception(f"Docstring for {self.value.eval(env)} not found")


class Mean():
    def __init__(self, data):
        self.data = data

    def eval(self, env):
        return statistics.mean(self.data.eval(env))


class SquareRoot():
    def __init__(self, data):
        self.data = data

    def eval(self, env):
        return math.sqrt(self.data.eval(env))


class Exit():
    def __init__(self, message):
        self.message = message

    def eval(self, env):
        sys.exit(self.message.eval(env))


class PathExists():
    def __init__(self, path):
        self.path = path

    def eval(self, env):
        return os.path.exists(self.path.eval(env))


class Wait():
    def __init__(self, time):
        self.time = time

    def eval(self, env):
        return time.sleep(self.time.eval(env))


class Hash():
    def __init__(self, expr):
        self.expr = expr
    
    def eval(self, env):
        return hash(self.expr.eval(env))


class LoopExpr():
    def __init__(self, value, expr):
        self.value = value
        self.expr = expr
    
    def eval(self, env):
        return [self.value, self.expr.eval(env)]

class For():
    def __init__(self, condition, eval_expr):
        self.condition = condition
        self.eval_expr = eval_expr
    
    def eval(self, env):
        for self.condition.eval(env)[0] in self.condition.eval(env)[1]:
            self.eval_expr.eval(env)


class Range():
    def __init__(self, val1):
        self.val1 = val1
    
    def eval(self, env):
        return range(self.val1.eval(env))