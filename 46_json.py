# json- Java Script Object Notation
# using it we can data parse etc.

import json
# json file has no comment, f=json file aved as .json extension
data = '{"var1":"ks", "var2":19}'
print(data)

parsed = json.loads(data)       #loads - parsed string into python dictionary.
print(parsed)       #here we can access by key,value pair.
print(parsed['var1'])
print(type(parsed))     #it will give which type is this?

#Task 1:- use of json.load
print("\tStarted reading of json file")
with open("kinu.json","r") as readfile:
    print("Converting json encoded data into python dictionary file")
    parsed = json.load(readfile)

print("Decoded json data from File")
for key, value in parsed.items():
    print(key, ":", value)
print("Done reading json file..")

#Task 2:- use of json.dump

data2 = {
    "channel_name":"Zee TV",
    "cars":['maruti alto', 'farari'],
    "fridge":('ice-cream','ice','chocolate'),        #tuple
    "isbad": False      #it will becomes json object, that's why F becomes small.
    }   #dictionary

jscomp = json.dumps(data2)
print(jscomp)

#Task 3:- what is sort keys parameter in dumps
# it will specify results should be sorted or not!.


p = json.dumps({"ks":2, "ram":1}, sort_keys=False)
print(p)