#   This is the basic use of classes and reusing them again and again. In the BankAccount class.

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(f"Deposited Amount : {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction.append(f"Withdrew Amount : {amount}")
        else:
            print("Insufficient Balance!!")

    def display(self):
        print(f"Account Holder :{self.name}")
        print(f"Balance : {self.balance}")
        print("Transaction History:")
        for transaction in self.transaction:
            print(f"- {transaction}")
        print("\n- Remaining Balance: Rs.", self.balance)

# Create instances of BankAccount
acc1 = BankAccount("Alice")
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(400)
acc1.display()