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
    
    def get_var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")
        
    def true(self):
        return True
    
    def false(self):
        return False
    
    def bool_comparison(self, expr, bool):
        if bool == "true":
            bool = self.true()
        elif bool == "false":
            bool = self.false()
        if expr == bool:
            return True
    
    def expr_comparison(self, expr1, expr2):
        if expr1 == expr2:
            return True
    
    def if_statement(self, condition, eval_expr):
        if condition:
            return eval_expr
        else:
            return
    