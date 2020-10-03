class Student:
    no_of_leaves = 8
    def __init__(self, name, num):
        self.name = name
        self.num = num

    @classmethod        #it is decorator
    def change_leaves(cls, newleaves):             #if we don't want to self argument then use it.
        cls.no_of_leaves = newleaves


kinjal = Student("kinjal", 35)

kinjal.change_leaves(43)
print(kinjal.no_of_leaves)          #no of leaves change 8 into 43 using class method.


#class method As alternative constructor.

class Stu:

    @staticmethod
    def printgood(string):
        print("this is " +string)
        #return "thenga"     #if we don't return anything then it will print none
    # @classmethod
    # def from_str(cls, string):
    #     params = string.split("-")
    #     print(params)
    #     return cls(params[0], params[1], params[2])
    #       return cls(*string.split("-"))


# kiran = Stu.from_str("kiran-76-kruti")
# print(kiran.salary)
priti = Stu()
print(priti.printgood("priya"))