# use of random module
import random
ran_num = random.randint(0, 6)      #it will generate random number between 0 to 6.
print(ran_num)
ran =random.random()        #it will generate random number between 0 to 1
print(ran)
ran1 = random.random()* 100     #it will generate random number between 0 to 100.
print(ran1)
lst = ("Star Plus","DD1","Zee Tv","Aaj Tak")
choice = random.choice(lst)     #it will randomely give us.
print(choice)


#learn new modules
import calendar         #it will display calender.
cal =calendar.month(2020,6)             #it will generate calender of full month
print("Here is the calender of month")
print(cal)
cal1 = int(input("Enter year:- "))
l = int(calendar.isleap(cal1))
if l == 1:
    print("is leap year")
else:
    print("not leap year")
print(cal1)

import winsound
winsound.PlaySound("gun_shot.wav",winsound.SND_ASYNC)

import math         #it will display all kind of maths function.
h = math.sqrt(4)
print("Square root:- ",h)

import platform     #it will display which platform on you are working.
x = platform.system()
print(x)

x = dir(platform)       #it will display all kind of directories.
print(x)