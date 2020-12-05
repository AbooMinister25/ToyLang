import os


class Importer():
    def __init__(self):
        self.modules = {}
        self.includes = ["PythonEvaluator"]
        self.builtins = ['filetools', 'jsontools']
        self.externals = [f for f in os.listdir("lite\external_modules") if os.path.isfile(os.path.join("lite\external_modules", f))]
    
    def import_module(self, modules):
        for module in modules:
            if module in self.builtins:
                x = __import__(f"modules.{self.builtins[self.builtins.index(module)]}")
                self.modules[module] = getattr(x, module)
            elif module in self.includes:
                x = __import__(f"modules.{self.includes[self.includes.index(module)]}")
                self.modules[module] = getattr(x, module)
            elif module in self.externals:
                x = __import__(f"external_modules.{self.externals[self.externals.index(module)]}")
                self.modules[module] = getattr(x, module)
            else:
                raise Exception(f"Unable to import module {module}")
