#wap to implement abstract classes and abstract 
from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,d1,d2):
        self.d1=d1
        self.d2=d2

    @abstractmethod
    def Area(self):
        pass

class circle(shape):
    def __init__(self,r):
        self.d1=r

    def Area(self):
        pi=3.14
        return (pi*self.d1*self.d1)

class rectangle(shape):
    def __init__(self,s1,s2):
        self.d1=s1
        self.d2=s2

    def Area(self):
        return (self.d1*self.d2)
    
c=circle(5)

r=rectangle(10,10)

print(c.Area())

print(r.Area())