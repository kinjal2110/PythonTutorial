#list
grosarry = ['shing', 'chana', 'mung-dal', 'pav', 'rice', 'chocolate']   #string list
print(grosarry)
print(grosarry[0])
number = [2, 4, 5, 7] #integer list
number.sort()       #it willl sort the list in ascending order
number.reverse()    #it will reverse the integer.
print(number)
print(number[2])    #number index start with 1
print(number[0:5:1])
print(number[0:5:2]) #in negative slicing -1 to negative number don't take.
number.append(8)    #append the end of list.
print(number)
number.insert(1,3)      #first position is index, second is number.
print(number)
number.remove(7)
print(number)