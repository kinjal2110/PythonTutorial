# we want to work on those who are last longer, but those function call half then between work.
def searcher():         #it is one kind of coroutine
    import time
    book = "This is a book on kinjal motivation.."
    time.sleep(4)           #some 4 seconds time consuming task, take time for read/downloading book etc.

    while True:
        text = (yield)     #yield means value to on the fly generate.
        if text in book:
            print("Your text in the book")
        else:
            print("Text is not in the book")

#--------------------------------coroutine--------------------------------------------
# it is used while they consume time to initialize then after work
search = searcher()     #it is coroutine.
print("Search started")
next(search)
print("Next method run!")
search.send("kinjal")       #this text find inside book variable. kinjal word there or not!.
input("Press any key: ")
search.send("This is")
input("press any key to continue: ")
search.send("motivation")
search.close()
search.send("hi")             #it will generate stp iteration error, bcz after close coroutine it will not work

