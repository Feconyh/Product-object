from register import *
class Stock():
    historic = []
    # function for add/Register products
    def add_product(code):
        check = False
        for i in range(len(Register.listwheel)): # Run the list and verify if this code exists already
            if code == Register.listwheel[i].code:
                check = True

        if check == True: # if so report back to the user
            print('This code already exists')

        elif check == False: # otherwise create a new product
            print(f'Code: {code}')
            description = str(input('Description: '))
            manufacturer = str(input('Manufacturer: '))
            amount = int(input('Amount: '))
            Register.create_list(code, description, manufacturer, amount)
  
    def reach_list(code):

        if code == '':
            for i in range(len(Register.listwheel)):
                print(Register.listwheel[i])
                print('='*30)
        else:
            code = int(code)
            check = False
            num = 0
            for i in range(len(Register.listwheel)):
                if code == Register.listwheel[i].code:
                    check = True
                    num = i

            if check == True:
                print(Register.listwheel[num])
                
                
            elif check == False:
                print('This code does not exists')

    def change(code):
        check = False
        for i in range(len(Register.listwheel)):
            if code == Register.listwheel[i].code:
                check == True
        
        if check == True:
            print('This code already exists')

        elif check == False:
            Register.listwheel[i].code = int(input('what id do you want to change to ?\n'))

            print(f'Now this is the new product code: {Register.listwheel[i].code}')
    
    def list_historic(choice, amount, code):
        if choice == 1: Stock.historic.append(f'{amount} purchase, of product of code: {code}')
        if choice == 2: Stock.historic.append(f'{amount} Sell, of product of code: {code}')
        
    def print_historic():
        for i in range(len(Stock.historic)):
            print('='*17,f'{i+1}','='*17)
            print(Stock.historic[i])