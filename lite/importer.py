import os


class Importer():
    def __init__(self):
        self.modules = {}
        self.builtins = ['filetools']
    
    def import_module(self, module):
        if module in self.builtins:
            x = __import__(f"modules.{self.builtins[self.builtins.index(module)]}")
            self.modules[module] = x.filetools
        else:
            raise Exception(f"Unable to import module {module}")
