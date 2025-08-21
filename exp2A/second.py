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