from manufacturer import *

# class Product
class Product():
    def __init__(self, code, description, manufacturer, amount):
        self.code = code
        self.description = description
        
        for i in manu.manufacturers:
            if i == manufacturer:
                self.manufacturer = i

        self.amount = amount

    def __str__(self):
        info = (f'{self.code}, {self.description}, {self.manufacturer}, {self.amount}')
        return info
