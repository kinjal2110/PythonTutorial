#file
# in voletile memory if you switched off the pc thn your data is in RAM which is crash/remove.
# while in voletile memory your memory is save for permenent.save like file.
'''
"r"- open file for reading- default mode
"w"- open file for writing
"x"- creates file if not exists, if file already exists then operation fail.
"a"- add more content to file at the end.
"t"- text mode, if we want to open in text format.
"b"- binary mode, if we want to open in binary format.
"+"- read and write, we can open file for update.
'''

f = open("kinjal.txt")
content = f.read()
print(content)
f.close()

print("\nfor read binary format")
f = open("kinjal.txt","rb")     #it will read in binary format.
content = f.read()
print(content)
f.close()


f = open("kinjal.txt")
content = f.read(6)     #it will read first 6 character
print(content)
f.close()

f = open("kinjal.txt", 'rt')
for line in f:
    print(line, end="")
f.close()

print("\n\nit will print line by line:-")
f = open("kinjal.txt","rt")
print(f.readline())
print(f.readline())     #it will read line by line character.
f.close()


print("\n")
f = open("kinjal.txt")
print(f.readlines())        #using readlines list is print
f.close()

f = open("kinjal.txt", "w")
f.write("kinjal love pavbhaji very much.")     #previous content remove and write new content on file.
f.close()

f = open("kinjal.txt","a")      #using this append mode we can append end of the line, withous removing old content.
f.write("\nkinjal like singing,coding,travelling,exploring new things.")
f.close()

f = open("kinjal.txt", "a")
t = f.write("hi.. cutie..")
print(t)        #it will return how much character you write.
f.close()


#we need to perform both operation read and write
f = open("kinjal.txt","r+")
print(f.read())
f.write("thank you")
f.close()

# file operation seek() and tell()
f = open("kinjal.txt")
print(f.tell())         #it will return your file pointer in which place(which character)-.
print(f.readline())
print(f.tell())
print(f.readline())
print(f.seek(10))       #it will reset pointer and pointer take to those position which we write.
print(f.readline())
f.seek(15)          #it will take file pointer into 15 character.
print(f.readline())
f.close()

# with block using open file
with open("kinjal.txt") as f:
    a = f.read(6)
    print(a)
f.close()