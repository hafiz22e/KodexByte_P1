class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} credited successfully.")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} debited successfully.")

    def balance_inquiry(self):
        print("Current Balance:", self.balance)


# ---- Main Program ----

# Create account (you can change values)
acc_no = int(input("Enter Account Number: "))
balance = float(input("Enter Initial Balance: "))

account = BankAccount(acc_no, balance)

while True:
    print("\n===== ATM MENU =====")
    print("1. Display Account")
    print("2. Credit Amount")
    print("3. Debit Amount")
    print("4. Balance Inquiry")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.display()

    elif choice == 2:
        amt = float(input("Enter amount to credit: "))
        account.credit(amt)

    elif choice == 3:
        amt = float(input("Enter amount to debit: "))
        account.debit(amt)

    elif choice == 4:
        account.balance_inquiry()

    elif choice == 5:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Try again.")
