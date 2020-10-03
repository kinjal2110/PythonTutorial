# recursion
def print2(str1):
    # print2(str1)      #it will generate recursion error.
    print("this is ",str1)

print2("kinjal")

'''
for factorial
n*n-1*n-2_n-3...n!
n!-n*(n-1)!
'''
def fact(num):
    f = 1
    for i in range(num):
        f = f*(i+1)
    return f


#for recursive factorial

def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)

number= int(input("Enter value: "))
print("factorial using iterative method: ",fact(number))
print("factorial using recursive method: ",fact_recursive(number))


# Quiz:  fibonacci series calculation
# 0 1 1 2 3 5 8

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n = int(input("Enter value for fibonacci: "))
print(fib(n))