# mapping operations to function
# using those kind of special (dunder) method we can achieve the concept of operator overloading
class Stud:
    no_of_stock = 9

    def __init__(self, name, eno, hobby):
        self.name = name
        self.eno = eno
        self.hobby = hobby

    def printData(self):
        return f"hi.. welcome.. it's my biodata"

    def __add__(self, other):           #it is secial method, it will help us for operator overloading
        return self.name + other.name

    def __truediv__(self, other):       #it will used for division
        return self.eno / other.eno

    def __repr__(self):
        return self.printData()

    def __str__(self):                  #first of all it will callled.
        return f"The name is {self.name}"

s = Stud("abc", 50, "programmer")
s1 = Stud("pqr", 10, "singing")
print(s + s1)
print(s / s1)
# print(s - s1)
print(s)