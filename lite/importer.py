import os


class Importer():
    def __init__(self):
        self.modules = {}
        self.builtins = ['filetools']
    
    def import(self, module):
        if module in self.builtins:
            x = __import__(f"lite.builtins.{self.builtins[module]}")
            self.modules[module] = x.builtins.filetools
        else:
            raise Exception(f"Unable to import module {module}")
    
    def check_ast(self, module, *tree):
        return self.modules[module].check_ast(tree)