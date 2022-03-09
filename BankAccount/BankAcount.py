class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)

    def yield_interest(self):
        self.balance *= interest_rate 

#Create 2 accounts
b1 = BankAccount(0, .01)
b2 = BankAccount(0, .05)


#Manipulating account 1  - why isnt yeild_interest working?...
b1.deposit(1000)
b1.deposit(2000)
#b1.yield_interest()
b1.display_account_info()


#Manipulating account 2 
b2.deposit(60000)
b2.deposit(10000)
b2.withdrawl(40000)
b2.withdrawl(2000)
b2.withdrawl(200)
b2.withdrawl(8000)
#b2.yield_interest()
b2.display_account_info()