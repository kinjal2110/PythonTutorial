# public : anyone can seen
# private : only family member can see.
# protected : only you can see those thing.

class Student:
    no_of_item = 5  #public variable
    _prot = 6       #protected variable
    __priv = 19     #private variable

    def __init__(self, name, eno, city):
        self.name = name
        self. eno = eno
        self.city = city

emp = Student("kinjal", 19, "bvn")
print(emp._prot)                        #protected variable will be printed.
print(emp._Student__priv)               #private variable direct can not derive, we need to derive by _class name.