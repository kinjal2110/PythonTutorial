'''
Itersble- __iter__() or __getitem__
Iterator __next__()
Iteration
'''
def gen(n):
    for i in range(n):
        # return i
        yield i         #it is return value

g =gen(3)
for i in g:
    print(i)

for i in range(6):
    print(i)

# using generator factorial
print("Factorial is: ")
def fact(n):
    sum = 1
    for i in range(n, 0):
        sum = sum * i
    yield sum           #it will generate value on the fly, saving ram

f = fact(4)
print(f)        #it will return memory location.

# ----------------------------------------iter, iterator, iteration------------------------------------

k = "kinjal"
print(iter(k))      #iter object address will return.
p = iter(k)
print("next: ",p.__next__())
print("next: ",p.__next__())
print("next: ",p.__next__())
print("next: ",p.__next__())
print("next: ",p.__next__())
print("next: ",p.__next__())
for c in k:
    print(c)        #string will print one by one character.        it is iterator