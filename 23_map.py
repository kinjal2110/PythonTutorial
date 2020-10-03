numbers = ["3", "2", "11"]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])        #if we can work on single line then no need to write every time for loop.

numbers[2] = numbers[2] + 1
print(numbers[2])

#----------------------------------------map-----------------------------------------
num = ["3", "5", "7"]
num = list(map(int, num))       #use of map function, we don't need to use about function.
print(num)

# -------------------------------------map with lambda-----------------------------------------------------
n = [2, 3, 4 ,5, 6, 7]
sq = list(map(lambda x:x*x, n))     #we already learn about lambda function, which will return us same work of function.
print(sq)

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))         #one side print square and another side cube.
    print(val)


#---------------------------------- use of filter-----------------------------------------
lst = [1, 2, 3, 4, 5, 6, 7, 8]

def is_greater_5(num):
    return num>5

gr_5 = list(filter(is_greater_5, lst))      #greater than 5 value will be printed
print(gr_5)

# -----------------------------------------reduce-------------------------------------
# using reduce we can improve performance as well as syntax becomes small.
from functools import reduce

l = [2,4, 6, 9]
num = 0
for i in l:
    num = num +i            #summation of whole list.
print(num)

l1 = [3, 6, 1, 4]
n = reduce(lambda x,y:x+y, l1)      #using reduce we don't need to write for loop
print(n)

l2 = [1, 2, 3, 4]
n1 = reduce(lambda x,y:x*y, l2)     #here 1*2*3*4
print(n1)