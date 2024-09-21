# WAP Create Account class with 2 attributes - balance & account no. 
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_on = acc
    
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balence())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balence())

    def get_balence(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(2000)
