# on soilder prettify my folder
'''
path give input
one file format
dictionary

def soldier("c://","ks.txt","jpg")      #it will capitalize first letter of all


'''
import os
def removeFiles(filen):
    DnotDis = open(filen)
    l = (DnotDis.read())
    var = (l.split("\n"))
    DnotDis.close()
    return var

def army(pathn, filen, ext):
    filen = filen
    pathn = pathn
    os.chdir(pathn)
    count = 0
    var = removeFiles(filen)
    for f in os.listdir():
        fname, fext = os.path.splitext(f)
        if fext == f".{ext}":
            newname = f"{str(count)}{fext}"
            count += 1
            os.rename(f, newname)
            pass
        if fname not in var:
            tn = fname.title()
            newname = f"{fname}{fext}"
        else:
            newname = f"{fname}{fext}"
        os.rename(f, newname)

    if __name__ == '__main__':
        pathn = input("Enter path name:")
        filen = input("Enter file name which contain nae of files not to alter: ")
        ext = input('Enter extension/format: ')
        army(pathn, filen, ext)
            