class Manufacturer():
    def __init__(self):
        self.manufacturers = []

    def add_manufacturer(self,new):
        self.manufacturers.append(new)


if __name__ == '__main__':
    manu = Manufacturer()
    manu.add_manufacturer('ford')

    for i in manu.manufacturers:
        if i == 'ford':
            print('sae mesmo')