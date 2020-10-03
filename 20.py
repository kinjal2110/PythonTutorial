# Enumarated function
l1 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
i = 1
for item in l1:
    if i is not 0:
        print(f"Day {i} are:- {item}")
    i+= 1

for index, item in enumerate(l1):
    if i%2 == 0:
        print(f" Days "
              f"{index} are: {item}")