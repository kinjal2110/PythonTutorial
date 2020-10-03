# use of multi level inheritance.
# dad class property derived in son, son class property derived in grandson.
class Dad:
    basketball = 1

class Son:
    dance = 1
    guitar = 1

    def isdance(self):
        return f'Yes I dance {self.dance} no. of times'

class GrandSon:
    dance = 6

    def isdance(self):
        return f"Jackson yeahh!.."\
               f"Yes I dance very awesomely {self.dance} no. of times."

dada = Dad()
papa = Son()
me = GrandSon()

print(me.isdance())
# Quiz:-
print(dada.basketball)

# Exercise:-
# make 3 class: 1-electronic device, 2 -pocket gadget, 3 -phone
# it will show multiple inheritance
class Electronic_Device:

    name = ("vivo", "samsung", "iphone")

    def __init__(self, cost, brand, version):
        self.cost =cost
        self.brand = brand
        self.version = version

class Pocket_Gadget(Electronic_Device):

    name = ("calculator", "phones", "pen")

    def printdetails(self):
        return f"the cost is {self.cost}, brand is {self.brand} and version is {self.version}"

class Phone(Pocket_Gadget):
    pass

vivo = Phone(15000, "y69", "7.0.6")
samsung = Phone(7000, "star pro", "6.8.3")
iphone = Phone(70000,"7","9.0.0")

print(samsung.printdetails())
print(vivo.printdetails())
print(iphone.printdetails())