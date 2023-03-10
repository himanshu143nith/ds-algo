
class Calculator(object):
    def __init__(self, *args):
        super(Calculator, self).__init__(*args)

    def addition(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b
