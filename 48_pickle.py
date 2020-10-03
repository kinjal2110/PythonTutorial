import pickle       #it means after preservation take at one place.
# everything is an object in python.
# pickle has lots of disadvantages.
#------------------------------------- pickling a python object-------------------------------------------
'''
cars = ["Audi", "Farari", "Maruti", "BMW"]
file = "mycar.pkl"      #pickle file write using .pkl extension.
fileobj = open(file, "wb")      #write on binary mode
pickle.dump(cars, fileobj)      #dump takes two argument, one is object another is one file object.
fileobj.close()
'''

file = "mycar.pkl"
fileobj = open(file, "rb")      #read binary mode on open file.
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))      #it is one kind of list.


# pickle.loads