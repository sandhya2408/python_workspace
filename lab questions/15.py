class Account:
    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = balance
    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print(f"after increment balance is {self.balance}")
    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount
        print(f"after  balance is {self.balance}")
    def show_info(self):
        print(f"account number:{self.accno} account name:{self.name} balance:{self.balance}")
ac1 = Account(10050,"sam",14456)
ac2 = Account(10551,"ram",45000)
ac1.show_info()
ac2.show_info()
ac1.deposit(10000)
ac1.show_info()
ac2.deposit(5000)
ac2.show_info()
ac1.withdraw(2000)
ac1.show_info
ac2.withdraw(1000)
ac2.show_info()

