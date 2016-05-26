class BinaryExpression:

    def __init__(self, op, expr1, expr2):
        if expr1 == None or expr2 == None:
            raise ValueError ("null expression argument")
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op

    def evaluate(self):
        if self.op == "ADD_OP":
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == "MUL_OP":
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == "SUB_OP":
            value = self.expr1.evaluate() - self.expr2.evaluate()
        else:
            value = self.expr1.evaluate() / self.expr2.evaluate()
        return value