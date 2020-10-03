from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod         #compulsory need to be implement this method.
    def printarea(self):
        return 0

class Rect(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 4

    def printarea(self):
        return self.length * self.breadth

r =Rect()
print(r.printarea())        #6 * 4
# tryobj = Shape()            #you can't make object of astract base class.