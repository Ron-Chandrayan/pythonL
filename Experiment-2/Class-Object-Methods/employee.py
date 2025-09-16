#Create Employee class to accept and display details of an employee

class Employee:
  def __init__(self):
    self.empid = 0
    self.name = " "
    self.salary = 0
  def accept(self):
    self.empid = int(input("Enter Employee ID: "))
    self.name = input("Enter name: ")
    self.salary = float(input("Enter salary: "))
  def display(self):
    print("Employee ID:", self.empid)
    print("Name:", self.name)
    print("Salary:", self.salary)

e = Employee()
e.accept()
e.display()