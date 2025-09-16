from abc import ABC, abstractmethod
class shape(ABC):
  def __init__(self, d1, d2):
    self.dim1 = d1
    self.dim2 = d2

  @abstractmethod
  def Area(self):
    pass

class Rectangle(shape):
  def __init__(self, d1, d2,):
    self.dim1 = d1
    self.dim2 = d2
  def Area(self):
    return self.dim1 * self.dim2

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
r = Rectangle(length, breadth)
print("Area of Rectangle: ", r.Area())