#dictionary is nothing but a key value pair.
d1=()
print(type(d1))     #it will make tuple
d2={}
print(type(d2))     #it will make dictionary
d3={"kinjal":"pavbhaji",
    "rutvika":"dhosa",
    "pinki":"utapam",
    "ks":{"b":"maggi","l":"roti","d":"samosa"}
    }
print(d3)
print(d3["kinjal"])     #it will return value
print(d3["ks"]["b"])    #it will return value of breakfast.
#immtable means no change. key value needs to be immutable.
d3["princy"]="junk food"
print(d3)
del d3["pinki"]     #it will delete pinki record.
print(d3)
print(d3.copy())    #it will return copy
d3.update({"rahu":"shing"})     #it will update
print(d3)
print(d3.keys())        #print all keys
print(d3.items())       #print all items


#use of set, using set unique value will display

s=set()
s_from_list = set([1, 2, 3, 4])
print(s_from_list)
print(type(s_from_list))        #it is type of class set.

#another way
s1 = [4, 5, 6, 7]
slist = set(s1)
print(slist)

s.add(1)
s.add(2)
s.add(4)
s1= s.union([1, 4,  3])     #it will return union value
print(s1)
s.remove(2)     #it will remove value
print(s)    #set return unique value
print(s.isdisjoint(s1))


#Exercise:- dictionary inside we can give key and value, we need to take user input as a key and we will give value of it.

dob= {'kinjal':'21/10/1999',
      'rutvika':'23-05-2002',
      "hetanshi":"25/12/2018",
      "yashraj":"311/05/2008"
      }
name = input("Enter the name:")
print(dob[name])