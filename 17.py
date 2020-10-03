# F strngs
me = "Kinjal"
a = "this is %s"%me     #string formating, here readability massup
print(a)
b = "ks"
c = "hi"
p = "%s %s"%(c, b)
print(p)

a1 = "hi.."
a2 = "how are you?"
a3 = "{1} {0}"      #{} {} blank also allowed.
b = a3.format(a1, a2)
print(b)



#concept of f string
import math
a2= "kinjal"
a = f"this is {a2} {math.sqrt(16)}"         #f means fast.
print(a)