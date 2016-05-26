import Memory

class Assignment :
    def __init__(self, var, expr) :
        if var == None :
            raise ValueError("null Id argument")
        if expr == None :
            raise ValueError("null Id argument")
        self.var = var
        self.expr = expr

    def execute(self):
        Memory.store(self.var.getChar(), self.expr.evaluate())