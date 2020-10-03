#string slicing
mystr = "Kinjal"
print(mystr[1])
print(mystr[3:6])     #string index start with 0.
print("it will return index of string:",len(mystr))
print(mystr[0:6:2])     #it will skip between character
print(mystr[::])        #if we don't give length then it will automatic whole length take

#negative index
print((mystr[-4]))      #minus count start from last character

#String functions
print(mystr.isalnum())  #if string between have space then boolean false return, otherwise true.
print(mystr.isalpha())
print(mystr.endswith("al"))     #if end with those character or not forchecking purpose it will used
print(mystr.endswith("df"))
print(mystr.count("a"))     #it will count how many time those character is arrived.
print(mystr.capitalize())       #it will capitalize to first letter.
print(mystr.find("a"))      #it will findd index location and return.
print(mystr.upper())        #it will convert to uppercase.
print(mystr.lower())        #it will convert to lowercase.
print(mystr.replace("K","m"))   #it will replace one string to another one.