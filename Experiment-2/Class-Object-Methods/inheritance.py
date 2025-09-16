#WAP to implement Inheritance between classes - Test Grade

class Test:
  def __init__(self, m1, m2, m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3

class Grade(Test):
  def __init__(self, m1,m2,m3):
    super().__init__(m1,m2,m3)
    self.totalmks = self.m1 + self.m2 + self.m3
    self.perc = (self.totalmks/300)*100

  def display_grade(self):
    if(self.perc >80):
      print("A")
    elif (self.perc > 60 and self.perc < 79):
      print("B")
    else:
      print("C")

marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

g = Grade(marks1, marks2, marks3)
print("Grade: ", g.display_grade())