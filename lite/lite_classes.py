class Environment():
    def __init__(self):
        self.vars = {}

    def get_variable(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception(f"Variable {name} not found")

    def assign_variable(self, name, value):
        if type(value) == str:
            value = value.strip('"')
        self.vars[name] = value
