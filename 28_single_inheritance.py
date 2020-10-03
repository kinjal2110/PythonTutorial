# for achieving abstraction we need to done encapsulation
# abstraction means part the work, in simple example:- if we buy computer then mouse is another complany, cpu
# another company, keyboard is also another company.in short different spare parts.
# encapsulation means details of hinding. hide implementation.

# inheritance means child class derived from parent class.
#use of single inheritance
class Employee:

    def printdetails(self):
        return f"name is {self.name}, salary is {self.salary} " #if we write inside self then we can use in any kind of objects.

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # pass            #if we don't implement anything then only write pass otherwise don't.

class Programmer:

    no_of_holidays = 65

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def print_prog(self):
        return f"name is {self.name} and salary is {self.salary}  and language know is {self.language}" #if we write inside self then we can use in any kind of objects.


Basit = Employee("basit", 4500)
Fiza = Employee("Fiza", 2000)

kinjal = Programmer("kinjal", 65000, ["python","php"])
rutvika = Programmer("rutvika", 430000, ["java", "c++"])

print(kinjal.print_prog())
print(rutvika.print_prog())
print(rutvika.no_of_holidays)