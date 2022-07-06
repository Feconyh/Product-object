from register import *

class Stock():
    def __init__(self):
        self.historic = []
        self.Register = Register()
        
    # function for add/self.Register products
    def add_product(self, code):
        check = False
        for i in range(len(self.Register.listwheel)): # Run the list and verify if this code exists already
            if code == self.Register.listwheel[i].code:
                check = True

        if check == True: # if so report back to the user
            print('This code already exists')

        elif check == False: # otherwise create a new product
            print(f'Code: {code}')
            self.description = str(input('Description: '))
            self.manufacturer = str(input('Manufacturer: '))
            self.amount = int(input('Amount: '))
            self.Register.create_list(code, self.description, self.manufacturer, self.amount)
  
    def reach_list(self, code):

        if code == '':
            for i in range(len(self.Register.listwheel)):
                print(self.Register.listwheel[i])
                print('='*30)
        else:
            code = int(code)
            check = False
            num = 0
            for i in range(len(self.Register.listwheel)):
                if code == self.Register.listwheel[i].code:
                    check = True
                    num = i

            if check == True:
                print(self.Register.listwheel[num])
                
                
            elif check == False:
                print('This code does not exists')

    def change(self, code):
        check = False
        check_again = False
        for i in range(len(self.Register.listwheel)):
            if code == self.Register.listwheel[i].code:
                check = True
                num = i
                
        if check == True:
            code = int(input('what id do you want to change to ?\n'))

            for i in range(len(self.Register.listwheel)):
                if code == self.Register.listwheel[i].code:
                    check_again = True
                
            if check_again == True:
                print(f'This code already exist in other')

            elif check_again == False:
                self.Register.listwheel[num].code = code
                print(f'Now this is the new product code: {self.Register.listwheel[i].code}')

        elif check == False:
            print('This code not exists')

    
    def list_historic(self, choice, amount, code):
        if choice == 1: self.historic.append(f'{amount} purchase, of product of code: {code}')
        if choice == 2: self.historic.append(f'{amount} Sell, of product of code: {code}')
        
    def print_historic(self):
        for i in range(len(self.historic)):
            print('='*17,f'{i+1}','='*17)
            print(self.historic[i])