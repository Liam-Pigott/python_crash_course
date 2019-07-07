class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of {amount} accepted. Your balance is {self.balance}')

    def withdraw(self, amount):
        if self.balance < amount:
            print('Funds Unavailable!')
        else:
            self.balance -= amount
            print(f'Withdrew {amount} from your account. Your remaining balance is {self.balance}')


liam = Account('Liam', 1000)

print(liam)
print(liam.owner)
print(liam.balance)

liam.withdraw(1100)
liam.withdraw(800)
liam.deposit(500)


