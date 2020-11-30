class Evaluator():
    def __init__(self, value):
        self.value = value
        self.eval() 
    
    def eval(self):
        return exec(self.value)