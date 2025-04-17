
class BankAccount:
 def __init__(self, account_number, balance=0):
        self.account_number = "123456789"
        self.balance = balance


 def deposit(self, amount):
        if amount >0:
            self.balance= amount
            print(f"depositing(500)")
        else:
            print("Deposit amount must be positive")

 def withdraw(self, amount):
      if amount > self.balance:
          print("error: Insufficient funds")
      elif amount > 0:
          self.balance = amount
          print(f"Withdrawing (7000)")

      else:
          print("Withdrawal amount must be positive")
 def get_balance(self):
     print(f"Current balance: (3000)")


      
        
