from control_moviment import *
from stock import *

# class that run this program
class Run():
    def __init__(self):
        self.Stock = Stock()
        self.Buy = Buy()
        self.Sell = Sell()
        

    def list(self):
        exit = False
        while exit == False:
            print('\n 1 - Register'
                '\n 2 - Reach Product'
                '\n 3 - Change Product'
                '\n 4 - Buy Product'
                '\n 5 - Sell Product'
                '\n 6 - historic'
                '\n 7 - Exit')

            decision = input('Your choice: ')

            if decision == '1':
                self.code = int(input('Which code you this product ?\n'))
                self.Stock.add_product(self.code)

            elif decision == '2':
                self.code = input('Which code do you want ?\n')
                self.Stock.reach_list(self.code)

            elif decision == '3':
                self.code = int(input('That the code of this product ?\n'))
                self.Stock.change(self.code)

            elif decision == '4':
                self.code = int(input('report the code of the product: '))
                self.Buy.purchase(self.code,self.Stock)

            elif decision == '5':
                self.code = int(input('report the code of the product: '))
                self.Sell.selling(self.code,self.Stock)
            
            elif decision == '6':
                self.Stock.print_historic()

            elif decision == '7':
                exit = True
                print('Good Bye')

            else:
                print('Value Invalid !')