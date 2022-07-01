from register import *
from stock import *

class Buy():
    def purchase(code,amount):

        for i in range(len(Register.listwheel)):
            if code == Register.listwheel[i].code:
                if amount <= Register.listwheel[i].amount and amount > 0:
                    print('Thank you, for the purchase here')

                    Register.listwheel[i].amount -= amount
                    
                else:
                    print('excuse me, we\'re out of stock')

            elif code != Register.listwheel[i].code:
                 print('excuse me, this product not exist')

class Sell():
    def selling(code,amount):

        for i in range(len(Register.listwheel)):
            if code == Register.listwheel[i].code:
                if amount > 0:
                    print('Thank you, for the sale here')

                    Register.listwheel[i].amount += amount

                if amount <= 0:
                    print('Please, report a valor true')
                    
            elif code != Register.listwheel[i].code:
                print('excuse me, this product not exist')
