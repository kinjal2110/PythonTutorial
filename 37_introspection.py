# python in everything is object
# object introspection means everything know about object that which class those object is derived
# and anything info. which type object.
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@99.com"

skill = Employee("skill", "F")
print(skill.email)

print(type(skill))                  #skill object is main function of employee class.
print(type("this is string"))       #it tis type of string class.
print(id("this is id"))             #it will return id of object.
print(id("hi"))

o = "this is dir"
print(dir(o))               #it will return all method, which can be used by us.

import inspect
print(inspect.getmembers(skill))

