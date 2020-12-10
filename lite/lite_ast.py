import random
import statistics
import os
import math
import sys
import time
import copy

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
            if self.functions[name]["args"] == None:
                if args != None:
                    raise TypeError("Invalid Arguments Given")
                return self.functions[name]["eval"].eval(self)
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
        return self.variables[name][index]
    
    def get_dict_keys(self, name):
        return [key for key in self.variables[name].keys()]
    
    def get_index(self, name, value):
        return self.variables[name].index(value)


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
    
    def type(self, env=None):
        return "String"


class TripleQuoteString():
    def __init__(self, value):
        value = value.strip()
        self.value = value.strip('"')
    
    def eval(self, env):
        return self.value
    
    def type(self, env=None):
        return "String"


class Integer():
    def __init__(self, value):
        self.value = int(value)

    def eval(self, env):
        return self.value
    
    def type(self, env=None):
        return "Integer"


class Array():
    def __init__(self, value):
        self.value = list(value)

    def eval(self, env):
        value = []
        for val in self.value:
            value.append(val.eval(env))
        return value
    
    def type(self, env=None):
        return "Array"


class AssignVariable():
    def __init__(self, name, value, type=None):
        self.name = name
        self.value = value
        self.type = type

    def eval(self, env):
        if self.type == "function":
            return env.assign_variable(self.name, env.call_function(self.value, None))
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
    
    def type(self, env):
        var_type = type(env.get_variable(self.name))
        if var_type == str:
            return "String"
        elif var_type == int:
            return "Integer"
        elif var_type == list:
            return "Array"
        elif var_type == dict:
            return "Dict"



class GetIndexValue():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self, env):
        return env.get_array_index(self.name, self.value.eval(env))


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
    
    def type(self, env=None):
        return "true"


class FalseBool():
    def __init__(self):
        self.value = False

    def eval(self, env):
        return self.value
    
    def type(self, env=None):
        return "false"


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
        
        self.local = Env()

    def eval(self, env):
        for expr in self.exprs:
            if type(expr) == Return:
                return expr.eval(self.local)
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


class ForBlock():
    def __init__(self, temp_var, exprs):
        self.exprs = exprs
        self.temp_var = temp_var

    def eval(self, env):
        for expr in self.exprs:
            expr.eval(env)

class For():
    def __init__(self, condition, eval_expr):
        self.condition = condition
        self.eval_expr = eval_expr
    
    def eval(self, env):
        pre_vars = copy.deepcopy(env.variables)
        for i in self.condition.eval(env)[1]:
            env.assign_variable(self.condition.eval(env)[0], i)
            self.eval_expr.eval(env)
        env.variables.clear()
        env.variables = pre_vars


class Range():
    def __init__(self, val1):
        self.val1 = val1
    
    def eval(self, env):
        return range(self.val1.eval(env))


class Import():
    def __init__(self, module):
        self.module = module
    
    def eval(self, env):
        return

class ModuleFunction():
    def __init__(self, function, arguments):
        if function == None and arguments == None:
            self.function = None
            self.arguments = None
        else:
            self.function = function
            self.arguments = arguments
    
    def eval(self, env):
        if self.function == None and self.arguments == None:
            pass
        else:
            try:
                evaled_args = [arg.eval(env) for arg in self.arguments]
            except Exception as e:
                evaled_args = self.arguments.eval(env)
            return self.function(*evaled_args)
        return


class IncludeEvaluator():
    def __init__(self, evaluator, data):
        self.evaluator = evaluator
        self.data = data
    
    def eval(self, env):
        return self.evaluator.Evaluator(self.data.eval(env))


class Dict():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def eval(self, env):
        return dict({self.key.eval(env): self.value.eval(env)})
    
    def type(self, env=None):
        return "dict"


class GetDictKeys():
    def __init__(self, name):
        self.name = name
    
    def eval(self, env):
        return env.get_dict_keys(self.name)


class GetIndex():
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def eval(self, env):
        return env.get_index(self.name, self.value.eval(env))


class GetType():
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        return self.value.type(env)


class Return():
    def __init__(self, value):
        self.values = value
    
    def eval(self, env):
        eval_values = []
        if len(self.values) == 1:
            return self.values[0].eval(env)
        for value in self.values:
            eval_values.append(value.eval(env))
        return eval_values