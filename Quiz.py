
#-----------------------------------------------------Quiz----------------------------------------------
#create a co-routine that takes input from user and return the file name, from 15 letters which it is  present
# or not.

def letter_search():
    print("Reading..")

    f1 = open("1.txt", 'a+')       #a+ create a file if not exist, append data and not overriding.
    f2 = open("2.txt", 'a+')
    f3 = open("3.txt", 'a+')
    f4 = open("4.txt", 'a+')
    f5 = open("5.txt", 'a+')
    f6 = open("6.txt", 'a+')
    f7 = open("7.txt", 'a+')
    f01 = f1.read()
    f02 = f2.read()
    f03 = f3.read()
    f04 = f4.read()
    f05 = f5.read()
    f06 = f6.read()
    f07 = f7.read()

    while True:
        text = (yield)
        # print("hello")
        if text in f01:
            print("found letter in 1.txt")
        elif text in f02:
            print("Found letter in 2.txt")
        elif text in f03:
            print("Found letter in 3.txt")
        elif text in f04:
            print("Found letter in 4.txt")
        elif text in f05:
            print("Found letter in 5.txt")
        elif text in f06:
            print("Found letter in 6.txt")
        elif text in f07:
            print("Found letter in 7.txt")
        elif text == "close":
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            f5.close()
            f6.close()
            f7.close()
            print("Closed all files")
        else:
            print("Not found")

search = letter_search()
print("it will start")
next(search)
while True:
    x = input("Enter a name to search in letters or quit: ")
    if x == "quit":
        print("Quiting... ")
        search.send("close")
        break
    else:
        search.send(x)