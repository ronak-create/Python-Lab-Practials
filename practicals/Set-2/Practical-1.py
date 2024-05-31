# class Account:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance+=amount
#         return f"Amount of ₹ {amount}/- has been deposited to you bank account, account number 'XX{int(str(self.account_number)[-4:])}'.\nCurrent balance = '{self.balance}'"
#     def Withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             return f"Amount of ₹ {amount}/- is debited from your bank account , account number 'XX{int(str(self.account_number)[-4:])}'.\nCurrent balance  = '{self.balance}'"
#         else:
#             return "Insufficient Balance."
# class Customer:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
# class Bank:
#     def __init__(self,name):
#         self.name = name
#         self.accounts = {}

#     def create_account(self, customer, initial_balance=0):
#         account_number = len(self.accounts)+1
#         new_account = Account(account_number,initial_balance)
#         self.accounts[account_number] = {'customer': customer,'account':new_account}
#         return new_account

# # obj = Bank('Ronak Parmar')
# #Main Code
# while True:
#     print("----------------------Welcome to Our Bank----------------------")
#     choice = ("Choose the query:\n1. Create an Account\n2. Withdraw\n3.Deposite\n>> ")
#     if choice == 1:
#         user = input("Enter your name: ")
#         initial_amt = int(input("Enter initial amount: "))
#         boj = Bank(user).create_account(user,initial_amt)
#     elif choice == 2:
#         boj = Bank(user).create_account(user,initial_amt)
#         newobj
#     # print(obj.create_account('Ronak Parmar',5000))
#     newobj = Account(1,5000)
#     print(newobj.Withdraw(200))

import random

class Customer:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.accounts = []

    def create_account(self, account_type, initial_balance):
        account_number = Bank.generate_account_number()
        account = BankAccount(account_type, initial_balance, self, account_number)
        self.accounts.append(account)
        return account

    def display_customer_info(self):
        #print(f"Customer Name: {self.name}")
        #print(f"Address: {self.address}")
        #print(f"Contact Number: {self.contact_number}")
        #print("Accounts:")
        
        for account in self.accounts:
            print(f"  - {account}")

class BankAccount:
    def __init__(self, account_type, balance, owner, account_number):
        self.account_type = account_type
        self.balance = balance
        self.owner = owner
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited INR {amount}. New balance: INR {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew INR {amount}. New balance: INR {self.balance}")
        else:
            print("Insufficient funds!")

    def __str__(self):
        return f"{self.account_type} Account - Account Number: {self.account_number}, Balance: ${self.balance}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    @staticmethod
    def generate_account_number():
        return ''.join(random.choice('0123456789') for _ in range(8))

    def display_bank_info(self):
        print(f"Bank Name: {self.name}")
        print("Customers:")
        for customer in self.customers:
            customer.display_customer_info()
            print()

    def find_account_by_number(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    return account
        return None


# Example usage
if __name__ == "__main__":
    # Create a bank
    my_bank = Bank("My Bank")
    customer_list=[]
    while True:
        print("1. New Customer 2. Existing Customer 3. Find Customers info 4.Exit")
        choice=int(input())
        if choice==1:
            print("Customer Registration: \n")
            # Create a customer
            name=input("Enter Customer Name:")
            address=input('Enter Customer Address: ')
            contact_number=input("Enter Customer Contact Number: ")
            customer_obj = Customer(name, address, contact_number)
            customer_list.append(customer_obj)
            my_bank.add_customer(customer_obj)
            while True:
               acc_type = int(input("Enter 1. To create Saving account 2. To Create Cheking account 3. Exit\n"))
               if acc_type == 1:
                  customer_obj.create_account("Savings", 1000)
                  print("Savings account Created\n")
                  break
               elif acc_type == 2:
                  customer_obj.create_account("Current", 1000)
                  print("Current account Created\n")
                  break
               elif acc_type == 3:
                   break
               else:
                    print("Invalid option....Try again")

        if choice==2:
            # User input for transactions
            account_number_input = input("Enter your account number: ")
            account_to_transact = my_bank.find_account_by_number(account_number_input)

            if account_to_transact:
                print(f"\nWelcome, {account_to_transact.owner.name}!")
                print(account_to_transact)
                while True:
                    print("1. Enter 1 to deposit\n2. Enter 2 to Withdrawl\n3. Enter 3 to Check the Balance\n4. Exit")
                    option=int(input("Enter your Option:\n"))
                    if option==1:
                        print("Welcome to Deposit Section\n")
                        # Deposit
                        deposit_amount = float(input("\nEnter the amount to deposit: INR "))
                        account_to_transact.deposit(deposit_amount)
                    elif option==2:
                        print("Welcome to withdrawl section:\n")
                        # Withdrawal
                        withdrawal_amount = float(input("\nEnter the amount to withdraw: INR "))
                        account_to_transact.withdraw(withdrawal_amount)
                    elif option==3:
                        # Display updated account information
                        print("\nUpdated Account Information:")
                        print(account_to_transact)
                    elif option==4:
                        break
                    else:
                        print("Invalid Option")
            else:
                print("Account not found.")
        if choice==3:
            my_bank.display_bank_info()
        elif choice==4:
            break
        else:
            pass