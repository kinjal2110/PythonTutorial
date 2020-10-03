import string
n1 = list(range(0,26))
n2 = list(range(27,53))
n3 = list(range(53,79))
test_list = list(string.ascii_lowercase)
l1 = []
l2 = []


def encr(s1):
    for idx, val in enumerate(s1):
        s2 = s1[idx:len(s1)]
        c1 = s1.count(val) - s2.count(val)
        num = test_list.index(val)
        if c1 % 3 == 0:
            l1.append(n1[num])
        elif c1 % 3 == 1:
            l1.append(n2[num])
        else:
            l1.append(n3[num])


def decr(l1):
    for idx,val in enumerate(l1):
        if val in range(0,26):
            l2.append(test_list[n1.index(val)])
        elif val in range(27,53):
            l2.append(test_list[n2.index(val)])
        else:
            l2.append(test_list[n3.index(val)])


s1 = input("Enter string:- \n")
s1 = s1.lower()
encr(s1)
decr(l1)
print(f"Your string is {s1}")
print("message after encryption is= ", end="")
print(*l1)
print("message after decryption is= ", end="")
print(*l2)
