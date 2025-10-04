class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")  # ✅ print exactly once
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")
