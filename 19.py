import time
# using time module we can initial time map.

initial = time.time()
print(initial)          #it will give initial time
k = 0
while(k <45):
    print("this is kinjal")
    time.sleep(2)       #this will wait for 2 seconds.
    k+=1
print(f"While loop ran in: {time.time()-initial} seconds")  #it will retrun which time duration complete while loop

initial2 = time.time()
for i in range(65):
    print("this is rutvika")
print(f"For loop ran in: {time.time()-initial2} seconds" )       #it will give which time duration complete for loop

# localtime
localtime = time.asctime(time.localtime(time.time()))       #it will return current time. asctime is return tuple into presentable format.
print(localtime)