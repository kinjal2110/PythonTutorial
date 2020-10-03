class A:
    def met(self):
        print("this is the method of class A")

class B(A):
    def met(self):
        print("this is the method of class B")

class C(A):
    def met(self):
        print("this is the method of class C")

class D(B, C):
    def met(self):
        print("This is the method of class D")

a = A()         #this is object
b = B()
c = C()
d = D()


print(d.met())