class BankAccount:
    def __init__(self, name, balance, interest_rate):
        self.name = name
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
        self.balance += self.balance * self.interest_rate


class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.account = BankAccount

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawel(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_user_balance(self):
        print(f"User :{self.name} , Balance: {self.amount}")
        return self


Kanye = BankAccount("Kanye", 1000, .01)
Eminem = BankAccount("Eminem",  800, .02)
SwaeLee = BankAccount("SwaeLee", 500, .03)

Kanye.make_deposit(200)
Kanye.make_deposit(600)
Kanye.make_deposit(400)
Kanye.make_withdrawel(300)
Kanye.display_user_balance()

Eminem.make_deposit(200)
Eminem.make_deposit(300)
Eminem.make_withdrawel(500)
Eminem.make_withdrawel(55)
Eminem.display_user_balance()

SwaeLee.make_deposit(140000)
SwaeLee.make_withdrawel(20)
SwaeLee.make_withdrawel(500)
SwaeLee.make_withdrawel(4500)
SwaeLee.display_user_balance()
