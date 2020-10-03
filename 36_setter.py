class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@99.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property               #it is decorator.
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set plz set it using setter"
        return f"{self.fname}.{self.lname}99@gmail.com"

    @email.setter               #we can set attributes.
    def email(self, string):
        print("setting now..")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter          #we can delete attribute using deletor
    def email(self):
        self.fname= None
        self.lname = None

hindustan =Employee("tirupati", "balaji")
pakistan =Employee("hayat", "mukaddar")

print(hindustan.explain())
print(hindustan.email)
hindustan.fname = "US"
print(hindustan.email)          #not change name bcz object is runtime in constructor.it will change after function return value.

hindustan.email = "this.ghdi@gmail.com"      #we need to set attribute, that's why we make setter method.
print(hindustan.email)

del hindustan.email         #we want to delete this attribute, so we need to deletor to delete it.
print(hindustan.email)