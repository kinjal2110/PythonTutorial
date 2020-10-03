#exercise:- faulty calculator.
'''
Design the calculator which will correctly sovle all the problem except following one:
 15*3= 786, 36+5= 37, 36/4=4, 88-43=23
 your program should take operator and two numbers from user and then return the resuls.
'''
print("\n Welcome to calculator, this is made by Kinjal Suryavanshi\n")
p1 = int(input("Enter first number:"))
p2 = int(input("Enter second number:"))
print("press + for addition")
print("press * for multiplication")
print("press / for division")
print("press - for substraction")
print("press % for modulus")
op = input("Enter operator:")
if(op=='+'):
    if(p1==36 and p2==5):
        print(37)
    else:
        p3=p1+p2
        print("Addition is: ",p3)

elif(op=='-'):
    if(p1==88 and p2==43):
        print(23)
    else:
        p3=p1-p2
        print("Substraction is: ",p3)

elif(op=='*'):
    if(p1==15 and p2==3):
        print(786)
    else:
        p3=p1*p2
        print("Multiplication is: ",p3)

elif(op=='/'):
    if(p1==36 and p2==4):
        print(4)
    else:
        p3=p1/p2
        print("Division is: ",p3)

elif(op=="%"):
    p3=p1%p2
    print("Modulus is: ",p3)

else:
    print("Invalid input")