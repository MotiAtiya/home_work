from classes.bank_account import BankAccount

account = BankAccount("Dana", 100)
account.deposit(50)
try:
    account.withdraw(500)
except ValueError as error:
    print("error:", error)
print(account.get_balance())
