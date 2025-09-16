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


class bank:
    def __init__(self):
        self.accno="XXXXXX"
        self.balance=100000

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("bank balance after deposit ",self.balance)
    
    def withdraw(self,amt):
        if(self.balance>amt):
            self.balance=self.balance-amt
            print("balance after withdraw ",self.balance)
        else:
            print("You are broke buddy ")

b= bank()
b.deposit(20000)
b.withdraw(30000)