# lambda function/anonymos function
'''
it is one line of function that's why we can call it anonymos function.
'''
def add(a,b):
    return a+b

add = lambda a,b : a+b      #work saem as function , here we don't need to create any kind of function.

# def a_first(a):
#     return a[1]

a= [[7, 3],[4, 6], [2, 9]]
a.sort(key=lambda  x:x[0])
print(a)