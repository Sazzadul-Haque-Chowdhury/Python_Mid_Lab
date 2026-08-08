from datetime import datetime

class BankAccount:
    next_account_number = 1000

    def __init__(self, balance, customer_name):
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1
        
        self.balance = float(balance)
        self.date_of_opening = datetime.now().strftime("%Y-%m-%d")
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"\n--- Account Details ---")
        print(f"Account Holder: {self.customer_name}")
        print(f"Account No: {self.account_number}")
        print(f"Opening Date: {self.date_of_opening}")
        print(f"Current Balance: {self.balance}\n")


print("--- Create a New Bank Account ---")
name = input("Enter customer name: ")
initial_balance = float(input("Enter initial balance: "))

my_account = BankAccount(initial_balance, name)
print(f"Account created successfully! Your assigned Account Number is: {my_account.account_number}")


while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        my_account.check_balance()
    elif choice == '2':
        dep_amount = float(input("Enter amount to deposit: "))
        my_account.deposit(dep_amount)
    elif choice == '3':
        draw_amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw(draw_amount)
    elif choice == '4':
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice! Please choose between 1 to 4.")