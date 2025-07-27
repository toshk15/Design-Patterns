class Pay:
    def pay(self, price):
        pass

class MasterCard(Pay):
    def pay(self, price):
        print("Pay ", price, "$ by MaterCard")

class VisaCard(Pay):
    def pay(self, price):
        print("Pay", price, "$ by VisaCard")

class Paypal(Pay):
    def pay(self, price):
        print("Pay", price, "$ by Paypal")

class PayManager:
    __pay = None

    def __init__(self, pay):
        self.__pay = pay

    def do_pay(self, price):
        self.__pay.pay(price)
    
print("You need to pay $25 for mobile phone")
code = int(input("please select payment method 1: MasterCard 2: VisaCard 3: Paypal \n"))


if code == 1:
    payManager = PayManager(MasterCard())
elif code == 2:
    payManager = PayManager(VisaCard())
elif code == 3:
    payManager = PayManager(Paypal())

payManager.do_pay(25)

        
        
