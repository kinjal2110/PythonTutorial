#global variable
l=10            #global scope/variable. global variable can't be changed.
def func1():
    # l=3         #local variable
    global l        #using global scope we take permission.
    l = l+4
    m=6
    # print(l)

func1()
print(l)
# print(m)        #local scope bcz error

def ks():
       x = 3
       def kinjal():        #nested function
           global x
           x = 19
       print("before calling kinjal(): ",x)     #both value are same because they find those on outside function.
       kinjal()
       print("after calling kinjal(): ",x)
ks()
print(x)        #it will find inside function that's why local variable scope print.

