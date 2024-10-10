# Base class (parent class)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner   # Public attribute
        self.__balance = balance  # Private attribute (encapsulation)

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount!")

    # Method to display balance
    def get_balance(self):
        return self.__balance

# Derived class (child class) inheriting from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)  # Inheriting from the parent class
        self.interest_rate = interest_rate

    # Method to add interest
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Added interest {interest}. New balance is {self.get_balance()}.")

# Creating objects of the class
account1 = BankAccount("John Doe", 500)
account1.deposit(300)
account1.withdraw(200)
print(f"Account balance: {account1.get_balance()}")

# Creating a savings account object
savings_account = SavingsAccount("Jane Doe", 1000, 0.05)
savings_account.add_interest()
savings_account.withdraw(500)
