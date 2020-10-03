
def simple_fun(a, b, c, d):
    print(a, b, c ,d)

simple_fun("pavbhaji", "dhosa", "samosa", "utapam")

def funargs(nor, *can_change, **kwargs):           #args and kwargs are optional.
    print(nor)
    for item in can_change:
        print(item)
    for key, value in kwargs.items():
        print(key, value)

can_change = ["kinjal", "rutvika"]      #it will goes as a tuple
nor = "this is "
# kw = ["krisha" :"coordinator"]  #dictionary
# funargs(nor, *can_change, **kw)