# ls = []
# for i in range(50):
#     if i%3==0:
#         ls.append(i)            #i module 3 ==0 value print
# above things we can also done by list comprehensions


# -----------------------------------------------list comprehension-----------------------------------
ls = [i for i in range(50) if i %3==0]      #it is list comprehension.
print(ls)

# dic = {0:"item0", 1:"item1"}        #simple method
#----------------------------------------dictionary comprehension----------------------------------------

dic = {
    i: f"Item {i}" for i in range(50) if i %2 ==0
}
dic1 = {value:key for key, value in dic.items()}     #using this dictionary will be decreasing order
print(dic)
print(dic1)

# -----------------------------------set comprehension-------------------------------------------------------
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress3"]}     #repeated value will be not print every time
print(dresses)
print(type(dresses))        #it is class set.


# -----------------------------------------generator comrehension--------------------------------------------
even = (i for i in range(50) if i % 2 ==0)
print(type(even))
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())