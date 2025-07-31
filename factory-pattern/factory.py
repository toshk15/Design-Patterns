class product:
    pass

class computer(product):
    def output(self):
        print("Dell computer")

class Mouse(product):
    def output(self):
        print("IBM Mouse")

class factory:
    @staticmethod
    def create(type):
        p = None
        if (type == 0):
            p = computer()
        elif (type == 1):
            p = Mouse()
        return p 
p = factory.create(0)
p.output()

p = factory.create(1)
p.output()
