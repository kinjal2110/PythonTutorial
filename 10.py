#functions
a = 9
b = 4
c = sum((a, b))     #sum is inbult function
print(c)

#user defifned function
def fun1():
    print("hello you are in function")
fun1()
fun1()


#function with argument
def fun2(a, b):
    """This is function which used to calculate average of two number"""
    avg=(a+b)/2
    print("Average is: ",avg)
print(fun2.__doc__)
fun2(3,4)
#function with return
def fun3(a,b):
    """This is the function which calculate sum of two number"""
    sum=a+b
    return sum
print(fun3.__doc__)
v=fun3(4,5)


print("Sum is: ",v)