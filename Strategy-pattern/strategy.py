class Strategy:
    def calculate(self, a, b):
        pass

class Addition(Strategy):
    def calculate(self, a, b):
        return a + b    

class Substraction(Strategy):
    def calculate(self, a, b):
        return a - b
    

class Context:
    __strategy = None

    def __init__(self, strategy):
        self.__strategy = strategy

    def do_calculate(self, a, b):
        return self.__strategy.calculate(a,b)
    
ctx = Context(Addition())
result = ctx.do_calculate(100, 200)
print("Adittion:",result)

    
ctx = Context(Substraction())
result = ctx.do_calculate(100, 200)
print("Subtraction:",result)


        