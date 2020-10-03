'''
Types of operators in python:
    Assignment operator
    comparison operator
    logical operator
    identity operator
    membership operator
    bitwise operator
    Arithmetic operaator
'''
print("use of arithmetic operator 5+6=",5+6)
print("use of arithmetic operator 5*6=",5*6)
print("use of arithmetic operator 5/6=",5/6)
print("use of arithmetic operator 7-6=",7-6)
print("use of arithmetic operator 5%6=",5%6)
print("use of arithmetic operator 14//6=",14//6)        #floor division operator
print("use of arithmetic operator 5**2=",5**2)

#if we need to assign value to the variable then we can use it.

print("\nAssignment operator")
x=5
print(x)
x+=7        #5+7
print(x)
x/=2        #12/2
print(x)
x-=3        #6-3
print(x)
x*=4        #3*4
print(x)
x%=5        #12%5
print(x)

print("\nComparision operaator")
i=5
print(i == 5)   #it will return true or false
print(i!= 5)
print(i <= 5)
print(i >= 5)

print("\nLogical operator")
a=True
b=False
c=True
print(a and b)      #true+false=false according to boolean algebra
print(a and c)      #true+true=true
print(a or b)       #any one is true then it will return true

print("\nIdentity operator")
print(a is b)
print(a is not b)       #a is not b that means a value is not same as value of b.
print(5 is 5)

print("\nMembership operator")
list= [3, 4, 5 ,7 ,2,1]
print(3 in list)
print(35 in list)       #it will check inside list or not.
print(35 not in list)

print("\nBitwise operator")
#it will work with bit, binary number.
'''
2=10
3=11
0=00
1=01
'''

print(0 & 1)
print(0 | 1)
print(0 | 3)        #0=00, 3=11 both has perform or operation then answer is 11=3.
print(0 & 2)        #0=00,2=10 both has perform and operation then answer is 00=0.



#short hand operator
a=int(input("\n\nEnter a: "))
b=int(input("Enter b: "))
if a>b: print("a  is greater")