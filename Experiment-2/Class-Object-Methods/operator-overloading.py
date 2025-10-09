#Create a fraction class to implement operator overloading for adding, subtracting and multiplying two fractions.

class fraction:
  def __init__(self, n = 0, d =1):
    self.num = n
    self.deno = d
  def __add__(self, other):
    self.num  = (self.num * other.deno) + (self.deno * other.num)
    self.deno = self.deno * other.deno
    return self.num, self.deno

f1 = fraction(5,6)
f2 = fraction(3,2)
f3 = f1 + f2  # + overloading for object addition
print(f3)