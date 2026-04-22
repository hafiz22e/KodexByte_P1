class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    # Display account details
    def display(self):
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)

    # Credit amount
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} credited successfully.")

    # Debit amount
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} debited successfully.")

    # Balance inquiry
    def balance_inquiry(self):
        print("Current Balance:", self.balance)


# ---- Main Program ----

# Create object
acc1 = BankAccount(12345, 1000)

# Display initial details
acc1.display()

# Credit money
acc1.credit(500)

# Debit money
acc1.debit(300)

# Check balance
acc1.balance_inquiry()
