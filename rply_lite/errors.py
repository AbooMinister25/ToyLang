from lark import Lark, Transformer, v_args
from lark.indenter import Indenter

class MainIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = ['LPAR', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RBRACE']
    INDENT_TYPE = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

@v_args(inline=True)
class MainTransformer(Transformer):
    def __init__(self):
        ...

    def number(self, value):
        return Integer(value)

    def string(self, value):
        value = str(value).strip('"')
        return String(value)

    def div(self, val1, val2):
        return Div(val1, val2)

    def print_statement(self, value):
        return Print(value)

    def if_statement(self, expr1, expr2, eval_expr):
        return If(expr1, expr2, eval_expr)

    def if_else_statement(self, expr1, expr2, eval_expr, else_statement):
        return If(expr1, expr2, eval_expr, else_statement)

    def if_statements(self, *values):
        for value in values:
            value.eval()

    def statement(self, *values):
        for value in values:
            value.eval()

grammar = '''
?start: expr*
      | statement* -> statement
      | if* -> if_statements

?if : "if" expr "==" expr "{" statement+ "}" -> if_statement
    | "if" expr "==" expr "{" expr+ "}" -> if_statement
    | "if" expr "==" expr "{" statement+ "}" "else" "{" statement+ "}" -> if_else_statement

?statement: "print" "(" expr ")" ";"  -> print_statement
          | "input" "(" expr ")" ";"  -> input_statement
          | NAME "=" expr ";"      -> assign_var
          | NAME "=" "input" "(" expr ")" ";" -> var_input_statement

?expr: STRING            -> string
     | NUMBER            -> number
     | NAME              -> get_var
%import common.ESCAPED_STRING -> STRING 
%import common.NUMBER
%import common.CNAME -> NAME
%declare _INDENT _DEDENT
%import common.WS_INLINE
%ignore WS_INLINE
%import common.NEWLINE -> _NL
%ignore _NL
'''
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

class If():
    def __init__(self, expr1, expr2, eval_expr, else_statement=None):
        self.expr1 = expr1
        self.expr2 = expr2
        self.eval_expr = eval_expr
        self.else_statement = else_statement

    def eval(self):
        if self.expr1.eval() == self.expr2.eval():
            return self.eval_expr.eval()
        else:
            if self.else_statement == None:
                return
            else:
                return self.else_statement.eval()

parser = Lark(grammar, parser='lalr', postlex=MainIndenter())
test_input = '''
if 5 == 5 {
    print("True");
}
else {
    print("False");
}
print("Done");
'''

if __name__ == '__main__':
    tree = parser.parse(test_input)
    print(MainTransformer().transform(tree))