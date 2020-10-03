a = input("What's your name:  ")
b = input("How much do you earn:  ")
if int(b) == 0:
    raise ZeroDivisionError("B is zero so stopping the program")        #general exception we can raise.

if a.isnumeric():
    # pass      #it will waste time so we take raise exception
    raise Exception("Numbers are not allowed!")

print(f"Hello {a}")

#1 thousand lines taking 1 hour
c = input("Enter name:  ")
try:
    print(a)

except Exception as e:
    if c == "kinjal":
        raise ValueError("Kinjal is blocked is not allowed")

    print("Variable is not defined")