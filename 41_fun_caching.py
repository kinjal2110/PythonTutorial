import time
from functools import lru_cache         #import lru_cache decrator

@lru_cache(maxsize=32)
def some_work(n):
    # Some task taking n seocnds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(2)
    print("calling again..")
    # input()                     #if you put any keyboard key then print.
    some_work(3)
    print("called again")



# ------------------------------lru_cache------------------------------------------------------
user = int(input("How many calculate do you want: "))
@lru_cache(maxsize=user)
def run_cache(userval):
    print("Run attemp1")
    time.sleep(3)
    print("Run attemp2")

if __name__ == '__main__':
    run_cache(user)