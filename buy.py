from register import *
    
class Buy():
    def shopping(code,amount):

        for i in range(len(Register.listwheel)):
            if code == Register.listwheel[i].code:
                if amount <= Register.listwheel[i].amount and amount > 0:
                    print('Thank you, for the purchase')

                    Register.listwheel[i].amount -= amount

                else:
                    print('excuse me, we\'re out of stock')