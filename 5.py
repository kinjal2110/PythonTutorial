#if, elif onditional statements.
'''
var1= 7
var2 = 9
print("Enter any value:")
var3 = int(input())

if var3 > var2:         #if any statement inside we want to go then put a colon
    print("greater")
elif var3 == var2:      #in python else if write like elif
    print("equal")
else:
    print("lesser")
'''


#using list check
list= [5, 6, 7]
if 5 in list:
    print("yes its inside the list")
print(6 in list)        #it will check inside tg=he list or not
print(3 in list)
print(6 not in list)        #it will true if not inside the list otherwise give false
print(2 not in list)


#Quiz        :- take user input as age, and check if user age is more then 18 then print "you can drive", if less then
#               18 then print "you can't drive" , if age is 18 then print "can't decide you need to come physically
#               then after we can decide you can drive or not.".

age = int(input("Enter your age here:"))
if  age > 18:
    print("you can drive")
elif age == 18:
    print("we can't decide you can drive or not, you need to come physically then after we can decide.")
else:
    print("you can't drive")




