
def fun1():
    print("Good Noon ")

fun2 = fun1     #function1 copied into function2
del fun1        #if we delete function1 then after it will call in function2
fun2()


def funret(num):
    if num == 0:
        return print
    if num ==1:
        return int
a = funret(1)       #1 for int, 0 for print
print(a)

def executor(func):
    func("this is ks")

executor(print)         #function return.


def decs(func11):
    def nowexec():
        print("Executing now")
        func11()
        print("Executed")
    return nowexec

@decs               #if we write upper @decs then below function becomes decorator.
def who_is_ks():        #this function is sendwich between those function which is decorator.
    print("ks is good girl")

# who_is_ks = decs(who_is_ks)           #second method to make decorator to the function
who_is_ks()