class Employee:
    def __init__(self):
        self.empid=0
        self.name=""
        self.salary=0
    
    def accept(self):
        self.empid=int(input("enter the empid "))
        self.name=input("enter string ")
        self.salary=int(input("enter the salary"))
    
    def display(self):
        print("Employee Details ")
        print("Emp-ID ",self.empid)
        print("Name ",self.name)
        print("salary ",self.salary)
    
e=Employee()
e.accept()
e.display()