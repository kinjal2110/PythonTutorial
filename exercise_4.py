
#exercise 4:- pattern printing
'''
take input from the user- integer n
boolean variable take- True or false

if true n=4
*
**
***
****

if false n=4
****
***
**
*

'''

n = int(input("Enter row number you want to print:-"))
s = int(input("type 1 or 0:-"))
new = bool(s)
if new == True:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("* ",end="")
        print()
elif new == False:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print("* ",end="")
        print()