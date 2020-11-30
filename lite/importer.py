import os


class Importer():
    def __init__(self):
        self.modules = {}
        self.includes = ["PythonEvaluator"]
        self.builtins = ['filetools']
    
    def import_module(self, module):
        if module in self.builtins:
            x = __import__(f"modules.{self.builtins[self.builtins.index(module)]}")
            self.modules[module] = getattr(x, module)
        elif module in self.includes:
            x = __import__(f"modules.{self.includes[self.includes.index(module)]}")
            self.modules[module] = getattr(x, module)
        else:
            raise Exception(f"Unable to import module {module}")
