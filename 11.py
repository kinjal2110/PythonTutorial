#exception
n1 = int(input("Enter number1: "))
n2 = input("Enter number2: ")
try:
    print("sum of number is: ",int(n1)+int(n2))
except Exception as e:
    print(e)

print("This line is very important need to print.")

# for comment we need to press ctr+/