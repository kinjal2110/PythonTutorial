# classes - Templates
# object - instance of class
# do not repeat yourself - decrease repeatablility

class Student:
    pass

yippi = Student()
gippi = Student()

yippi.name = "yippi gupta"
yippi.std = 12
yippi.section = 1
yippi.subjects = ['hindi', 'english', 'science']
gippi.name = "gippi tripathi"
print(yippi, gippi)#it will reurn memory location.
print(yippi.name)
print(gippi.name)
print(yippi.subjects)