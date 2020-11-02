from lark import Lark, Transformer, v_args

@v_args(inline=True)    # Affects the signatures of the methods
class LiteTransformer(Transformer):
    number = int
    string = str

    def __init__(self):
        self.vars = {}

    def add(self, val1, val2):
        return int(val1) + int(val2)

    def sub(self, val1, val2):
        return int(val1) - int(val2)

    def mul(self, val1, val2):
        return int(val1) * int(val2)

    def div(self, val1, val2):
        return int(val1) / int(val2)

    def str_add(self, val1, val2):
        val1 = val1.strip('"')
        val2 = val2.strip('"')
        return str(val1) + str(val2)

    def print_statement(self, value):
        value = str(value).strip('"')
        return value

    def input_statement(self, value):
        value = str(value).strip('"')
        input(value)
    
    def assign_var(self, name, value):
        if type(value) == str:
            value = value.strip('"')
        self.vars[name] = value
        return value
    
    def get_var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")
    
    def if_statement(self, condition, eval_expr):
        if condition:
            eval_expr
