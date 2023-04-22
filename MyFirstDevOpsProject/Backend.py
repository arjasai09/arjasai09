class BankAccount:
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(("Deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(("Withdrawal", amount))

    def display_balance(self):
        print(f"Account Name: {self.account_name}")
        print(f"Current Balance: {self.balance}")
        
    def display_transactions(self):
        print(f"Account Name: {self.account_name}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"{transaction[0]}: {transaction[1]}")

my_account = BankAccount("John Doe", 1000)

my_account.deposit(500)
my_account.withdraw(400)

my_account.display_balance()
# Output: 
# Account Name: John Doe
# Current Balance: 1300

my_account.display_transactions()
# Output:
# Account Name: John Doe
# Transaction History:
# Deposit: 500
# Withdrawal: 200
