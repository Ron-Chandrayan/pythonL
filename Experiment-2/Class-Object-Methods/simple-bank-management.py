#Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transcations 
class Bank:
  def __init__(self):
    self.accNum = 0
    self.balance = 0
    self.transactions = []
    self.accName = " "
  def accept(self):
    self.accName = input("Enter account name: ")
    self.accNum = int(input("Enter account number: "))
    
    while True:
      choice = int(input("Enter 1 to deposit or 2 to withdraw or 3 to exit: "))
      if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")
      elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
          print("Insufficient balance.")
        else:
         self.balance -= amount
         self.transactions.append(f"Withdraw: {amount}")
      elif choice == 3:
        break
      else:
        print("Enter 1 or 2 or 3.")
    
  def display(self):
    print("Account Name:", self.accName)
    print("Account Nu-mber:", self.accNum)
    print("Balance", self.balance)
    print("Transactions:", self.transactions)

b = Bank()
b.accept()
b.display()