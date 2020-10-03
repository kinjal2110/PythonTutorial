f1 = open("kinjal.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)                #we are printing exception here.

except EOFError as e:       #end of file error.
    print(e)

except IOError as e:        #input/output error.
    print(e)

else:
    print("This will run only if except is not running.")
#----------------------------------finally----------------------------------------------------
# finally run for code clean up.
finally:
        print("Run this anyways")
        f1.close()
        # f.close()

print("Important Stuff")