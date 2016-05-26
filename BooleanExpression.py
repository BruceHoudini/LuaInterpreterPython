class BooleanExpression:
    def __init__(self, op, expr1, expr2):
        if expr1 == None or expr2 == None:
            raise ValueError("null expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.op == "LE_OP":
            return self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == "LT_OP":
            return self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == "GE_OP":
            return self.expr1.evaluate() >= self.expr2.evaluate()
        elif self.op == "GT_OP":
            return self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == "EQ_OP":
            return self.expr1.evaluate() == self.expr2.evaluate()
        else:
            return self.expr1.evaluate() != self.expr2.evaluate()