# oop is organized things easily.
#code reusability increases.

class Employee:
    no_of_lives = 8

    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}" #if we write inside self then we can use in any kind of objects.

Basit = Employee()
Fiza = Employee()

Basit.name = "Basit"
Basit.salary = 6677
Basit.role = "instructor"

Fiza.name = "Fiza"
Fiza.salary = 8000
Fiza.role = "accountant"

print(Fiza.name)
print(Basit.no_of_lives)        #we can access by instance variable
print(Employee.no_of_lives)     #we can access by class also
# we can only change class variable by class not instance variable
Employee.no_of_lives = 10           #instance variable can't change property of class variaable.
print(Employee.no_of_lives)
Fiza.no_of_lives = 13
print(Fiza.no_of_lives)         #it will make new instance variable using same name, it will not change in class variable.
print(Employee.no_of_lives)     #hence prove that employee variable value as it is.
print(Basit.__dict__)           #it will return dictionary
print(Employee.__dict__)

print(Fiza.printdetails())      #function call


#Use of constructor
# it will automatically construct object
class Stu:
    def __init__(self, aname, abranch, anum):
        self.name = aname
        self.branch = abranch
        self.num = anum


ks = Stu("kinjal", "IT", 19)         #name, branch, num
print(ks.name)
print(ks.branch)
print(ks.num)