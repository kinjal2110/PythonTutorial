# Health Management System
# 3 clients we need to manage their diet- harry, rohan and hammad
# total 6 files need to make
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client
'''
first of all user to ask which you want to lock: 1 for harry, 2 for rohan or 3 for hammad.
then after we lock 1 for harry then they ask us to lock exercise for 1 or diet for 2.then after select any one of
 then then msg will be display you successfully write.
'''
i = 0
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise 2 for diet"))
        if(c==1):
            value = input("type here\n")
            with open("ks.txt","a") as op:      #here we can append
                op.write(str([str(gettime())])+ ": "+value+"\n")
            print("successfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("ks_food.txt","a") as op:
                op.write(str([str(gettime())])+ ": "+value+"\n")
        else:
            print("Please enter valid input (1(ks),2(kinjal))")

    elif k == 2:
        c = int(input("Enter 1 for exercise 2 for diet plan: "))
        if(c == 1):
            value= input("type here\n")
            with open("kinjal.txt","a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("kinjal_food.txt","a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
        else:
            print("Please enter valid input (1(ks),2(kinjal))")

def retrieve(k):
    if k ==1:
        c = int(input("Enter 1 for exercise 2 for diet plan:- "))
        if c == 1:
            with open("ks.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c ==2:
            with open("ks_food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif k == 2:
        c = int(input("Enter 1 for exercise 2 for diet plan:- "))
        if c == 1:
            with open("kinjal.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c == 2:
            with open("kinjal_food.txt") as op:
                for i in op:
                    print(i, end=" ")
    else:
        print("Please enter valid input (ks, kinjal)")
print("Health Management System")
a = int(input("Press 1 for log the value or 2 for retrieve the value:- "))
if a == 1:
    b = int(input("Press 1 for ks 2 for kinjal:- "))
    take(b)
else:
    b = int(input("Press 1 for ks  2 fork kinjal:- "))
    retrieve(b)