from lark import Lark, Transformer, v_args

grammar = r"""
start: file_find*

?file_find: "file_find" "(" expr ")"

"""

class FileFind():
    def __init__(self, filename):
        self.filename = filename
    
    def eval(self, env):
        return self.filename.eval(env)


class MainTransformer(Transformer):
    def __init__(self):
        ...
    
    def file_find(self, filename):
        return FileFind(filename)

