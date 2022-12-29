class BankAccount():
    def _init_(self, username, balance):
        self.username = username
        self.balance = balance
        print(self.username)
        print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            try:
                0 / 0
            except:
                print("no available balance")
        else:
            print(self.username)
            print("withdrawl completed")

    def deposit(self, amount):
        self.amount = amount
        print(self.amount)
        if amount > 1000:
            try:
                0 / 0
            except:
                print("limit exceeded")
        else:
            self.balance += amount
