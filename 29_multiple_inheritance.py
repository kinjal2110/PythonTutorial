#use of multiple inheritance
# one class property into inherit multiple class
class Employee:         #base class
    var = 6

    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} " #if we write inside self then we can use in any kind of objects.

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Player:           #derived class
    var = 8
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"this is {self.name} and game is {self.game}"

class CoolEmployee(Employee, Player):           #derived class

    language = "c++"
    var =10

    def printLanguage(self):
        print(self.language)

Basit = Employee("basit", 4500)
Fiza = Employee("Fiza", 2000)

shruti = Player("shruti", ["kho-kho"])

shreya = CoolEmployee("shreya",67000)
det = shreya.printdetails()
print(det)
shreya.printLanguage()
print(shreya.var)       #variable print of CoolEmployee class
print(shruti.var)       #variable print of Player class
print(Basit.var)        #variable print of Employee class
