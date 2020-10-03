import sklearn
def printks(string):
    return f"hiee. this is kinjal {string}"

def add(num1, num2):
    return num1 + num2 +5
# import tutMain2
print("name value: ",__name__)      #this value will be only __main__ if this will be run on original/same program.
# if name value is main then execute otherwise don't execute it.
if __name__ == '__main__':          #this content will not used on another imported file.
    print(printks("Suryavanshi"))
    o = add(5,6)        #5+6+5
    print(o)