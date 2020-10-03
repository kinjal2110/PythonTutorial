#loops
list1= [ ['kinjal',1], ['chocolate',3], ['cake',2], ['pavbhaji',3], ['apple',1] ]
dict1 = dict(list1)
for item, lollypop in dict1.items():
    print(item, "and quantity is ",lollypop)

for item in dict1:      #it will give you only key.
    print(item)

#Quiz:- make a list,we need to detect number or not, if number then check  greater then 6 or not and print it.
l1 = [6, 7,4,9,"priya", "mekhiya", 'prajapati', 76]
for item in l1:
    if str(item).isnumeric() and item>6:
        print(item)

#while loop
'''
i=0
while(i<5):
    print(i)
    i=i+1
'''
i=0
print("greater than 5 value will be print here")
while(True):
    if i+1<5:
        i=i+1
        continue
#below staatement will not work while continue
    print(i + 1)
    if(i==9):
        break #stop the loop
    i=i+1

# Quiz: take number through user input, if those number will greaater then 100 then print congo.. , otherwise till
#       take the input through the user unless 100.
n=0
while(True):
    n=int(input("Enter number:\n "))
    if(n<100):
        print("try again")
        continue

    else:
        print("congratulations you will come up to 100.")
        break