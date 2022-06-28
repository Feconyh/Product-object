# class Product
class Product():
    def __init__(self, code, description, manufacturer, amount):
        self.code = code
        self.description = description
        self.manufacturer = manufacturer
        self.amount = amount

class Cansei():
    def list():
        exit = False
        while exit == False:
            print('\n 1 - Register'
                '\n 2 - List All'
                '\n 3 - Reach Product'
                '\n 4 - Change Product'
                '\n 5 - Exit')

            decision = int(input('Your choice: '))

            if decision == 1:
                code = int(input('Which code you this product ?\n'))
                Cansei.add_product(code)

            elif decision == 2:
                print('='*30)
                Cansei.list_all()

            elif decision == 3:
                code = int(input('Which code do you want ?\n'))
                Cansei.list_one(code)

            elif decision == 4:
                code = int(input('That the code of this product ?\n'))
                Cansei.change(code)

            elif decision == 5:
                exit = True
                print('Good Bye')

            else:
                print('Value Invalid !')
    
    def add_product(code):
        check = False
        for i in range(len(Cadaster.listwheel)):
            if code == Cadaster.listwheel[i].code:
                check = True

        if check == True:
            print('This code already exists')

        elif check == False:
            print(f'Code: {code}')
            description = str(input('Description: '))
            manufacturer = str(input('Manufacturer: '))
            amount = int(input('Amount: '))
            Cadaster.create_list(code, description, manufacturer, amount)
  
    def list_all():
        for i in range(len(Cadaster.listwheel)):
            print(Cadaster.listwheel[i].code)
            print(Cadaster.listwheel[i].description)
            print(Cadaster.listwheel[i].manufacturer)
            print(Cadaster.listwheel[i].amount)
            print('='*30)

    def list_one(code):
        check = False
        for i in range(len(Cadaster.listwheel)):
            if code == Cadaster.listwheel[i].code:
                check = True

        if code == True:
            print(Cadaster.listwheel[i].code)
            print(Cadaster.listwheel[i].description)
            print(Cadaster.listwheel[i].manufacturer)
            print(Cadaster.listwheel[i].amount)
            
        elif check == False:
            print('This code does not exists')
        
    def change(code):
        check = False
        for i in range(len(Cadaster.listwheel)):
            if code == Cadaster.listwheel[i].code:
                check == True
        
        if check == True:
            print('This code already exists')

        elif check == False:
            Cadaster.listwheel[i].code = int(input('what id do you want to change to ?\n'))

            print(f'Now this is the new product code: {Cadaster.listwheel[i].code}')

class Cadaster():
    listcount = 0
    listwheel = []

    def create_list(code, description, manufacturer, amount):
        Cadaster.listwheel.append(Cadaster.listcount)
        Cadaster.listwheel[Cadaster.listcount] = Product(code, description, manufacturer, amount)
        Cadaster.listcount += 1

        print(Cadaster.listwheel[Cadaster.listcount-1].code)

if __name__ == '__main__':
    Cadaster.create_list(1, 's', 's', 1)
    Cansei.list()
