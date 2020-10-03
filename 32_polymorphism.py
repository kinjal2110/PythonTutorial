# polymorphism means ability to take many forms.
class A:
    cvar1 = "I am in class A"
    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.cvar1 = "Instance variable of class A"
        self.special = "you are special!"

class B(A):
    var2 = "I am in class B"
    def __init__(self):             #constructor overrriding.
        super().__init__()                  #super class
        self.var1 = "I am inside class A constructor"
        self.cvar1 = "Instance variable of class A"

a = A()
b = B()

print(b.cvar1)
print(b.special)
print(b.var2)