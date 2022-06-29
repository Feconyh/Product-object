from product import *

class Register():
    listcount = 0
    listwheel = []

    def create_list(code, description, manufacturer, amount):
        Register.listwheel.append(Register.listcount)
        Register.listwheel[Register.listcount] = Product(code, description, manufacturer, amount)
        Register.listcount += 1