class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operators = operands

    def add(self):
        pass

    def substract(self):
        difference =0
        for item in self.operators:
            difference -= item
        print(difference)

    def divide(self):
        pass

    def multiply(self):
        if self.operators is None:
            return
        product = 1
        product  = 1
        for item in self.operators:
            product *= item
        print(product)