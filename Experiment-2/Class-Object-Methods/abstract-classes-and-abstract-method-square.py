#WAP to implement abstract classes and abstract methods - square
from abc import ABC, abstractmethod
class shape(ABC):
  def __init__(self, d1, d2):
    self.dim1 = d1
    self.dim2 = d2

  @abstractmethod
  def Area(self):
    pass

class circle(shape):
  def __init__(self, r,):
    self.dim1 = r
  def Area(self):
    pi = 3.14
    return pi * self.dim1 * self.dim1

radius = int(input("Enter radius of the circle: "))
c = circle(radius)
print("Area of circle: ", c.Area())