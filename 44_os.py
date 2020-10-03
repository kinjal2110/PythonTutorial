import os       #it is built in modules.
print(dir(os))      #it will display all kind of modules whichever used in os.
print(os.getcwd())      #it will disolay current directory.
os.chdir("c:/")      #it will change the directory
print(os.getcwd())
print(os.listdir("c://"))     #folder all directory display in list form.
# os.mkdir("hi.txt")
# os.makedirs("osmake/that")
# os.rename('hi.txt', "kin.txt")
print(os.environ.get('path'))       #your already setting environment variable will be show.
print(os.path.join("c:/","/ks.txt"))        #it will join two paths efficiently.
print(os.path.exists("c://"))           #it will return boolean value path exists or not.
print(os.path.exists("c://ks.txt"))         #it will not exist.
print(os.path.isfile("c://ks.txt"))     #it will say file exist or not.
print(os.path.isdir("c://ks.txt"))      #it will return directory or not.
