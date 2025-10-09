#WAP to implement abstract classes and abstract methods - triangle
from abc import ABC, abstractmethod
class shape(ABC):
  def __init__(self, d1, d2):
    self.dim1 = d1
    self.dim2 = d2

  @abstractmethod
  def Area(self):
    pass

class Triangle(shape):
  def __init__(self, d1, d2):
    self.dim1 = d1
    self.dim2 = d2
  def Area(self):
    return 0.5*self.dim1 * self.dim2

base= int(input("Enter base: "))
height = int(input("Enter height: "))
t = Triangle(base, height)
print("Area of Triangle: ", t.Area())