class Laptop:
    def brand(self,name):
        print("The brand of the laptop is",name)

    def price(self,price):
        print("The price of the laptop is",price)


class Dell(Laptop):
    
    def quantity(self,quantity):
        print("The quantity of the laptop is",quantity)


class Toshiba(Laptop):
    pass



dojb = Dell()
tojb = Toshiba()
dojb.brand("Dell")
tojb.brand("Toshiba")
