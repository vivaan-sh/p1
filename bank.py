class BankAccount:
    bank_name = "HDFC Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, initial_deposit):
        self.account_holder = account_holder
        self.balance = initial_deposit

        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print("Deposit Successful!")
            print("Updated Balance:", self.balance)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print("Withdrawal Successful!")
            print("Updated Balance:", self.balance)

    def display_account_info(self):
        print("\n----- Account Information -----")
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Account Balance:", self.balance)
        print("--------------------------------")

    @classmethod
    def display_bank_info(cls):
        print("\n===== Bank Information =====")
        print("Bank Name:", cls.bank_name)
        print("Total Accounts:", cls.total_accounts)
        print("Total Bank Balance:", cls.total_bank_balance)
        print("==============================")


def main():
    accounts = {}

    while True:
        print("\n====== BANK MENU ======")
        print("1. CREATE ACCOUNT")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. DISPLAY ACCOUNT INFO")
        print("5. DISPLAY BANK INFO")
        print("6. EXIT")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            initial = float(input("Enter initial deposit: "))
            account = BankAccount(name, initial)
            accounts[name] = account
            print("Account created successfully!")

        elif choice == "2":
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":  
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            name = input("Enter account holder name: ")
            if name in accounts:
                accounts[name].display_account_info()
            else:
                print("Account not found!")

        elif choice == "5":
            BankAccount.display_bank_info()  

        elif choice == "6":
            print("Thank you for using National Bank System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()