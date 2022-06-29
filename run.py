from stock import *
from buy import *

# class that run this program
class Run():
    def list():
        exit = False
        while exit == False:
            print('\n 1 - Register'
                '\n 2 - Reach Product'
                '\n 3 - Buy Product'
                '\n 4 - Change Product'
                '\n 5 - Exit')

            decision = input('Your choice: ')

            if decision == '1':
                code = int(input('Which code you this product ?\n'))
                Stock.add_product(code)

            elif decision == '2':
                code = input('Which code do you want ?\n')
                Stock.reach_list(code)

            elif decision == '3':
                code = int(input('report the code of the product: '))
                amount = int(input('report the amount: '))

                Buy.shopping(code,amount)

            elif decision == '4':
                code = int(input('That the code of this product ?\n'))
                Stock.change(code)

            elif decision == '5':
                exit = True
                print('Good Bye')

            else:
                print('Value Invalid !')