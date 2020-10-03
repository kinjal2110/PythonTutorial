# == - value equality- two object have the same value
# is - reference equality- two references refer same object.

#Task
a = [6, 4, "56"]
b = [6, 4, "56"]
print(b is a)
print(a == b)       #true
a = b
print(a is b)       #we need to reference to a value to the b then after it will return true.




#python 2.3 vs 3.7
# print 'hi'    #syntax of python 2.3