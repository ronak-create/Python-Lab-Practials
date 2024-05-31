import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
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
        return f"Customer Name: {self.name}\nAddress: {self.address}\nContact Number: {self.contact_number}\nAccounts:\n" + \
               "\n".join([f"  - {account}" for account in self.accounts])

class BankAccount:
    def __init__(self, account_type, balance, owner, account_number):
        self.account_type = account_type
        self.balance = balance
        self.owner = owner
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited INR {amount}. New balance: INR {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew INR {amount}. New balance: INR {self.balance}"
        else:
            return "Insufficient funds!"

    def __str__(self):
        return f"{self.account_type} Account - Account Number: {self.account_number}, Balance: INR {self.balance}"


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
        return f"Bank Name: {self.name}\nCustomers:\n" + "\n\n".join([customer.display_customer_info() for customer in self.customers])

    def find_account_by_number(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    return account
        return None

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bank Application")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.bank = Bank("My Bank")

        self.customer_list = []
        self.current_account = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Bank Application", font=("Helvetica", 24), bg="#f0f0f0")
        self.label.pack(pady=20)
        
        self.menu_label = tk.Label(self, text="1. New Customer 2. Existing Customer 3. Find Customers info 4.Exit", font=("Helvetica", 12))
        self.menu_label.pack(pady=10)

        self.menu_label = tk.Label(self, text="Choose an option:", font=("Helvetica", 14), bg="#f0f0f0")
        self.menu_label.pack(pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.insert(0, "1")

        self.submit_button = ttk.Button(self, text="Submit", command=self.process_choice)
        self.submit_button.pack(pady=15)

        self.output_text = tk.Text(self, height=15, width=60, font=("Helvetica", 12))
        self.output_text.pack(pady=20)

    def process_choice(self):
        choice = self.entry_var.get()

        if choice == "1":
            self.register_customer()
        elif choice == "2":
            self.existing_customer()
        elif choice == "3":
            self.display_customers_info()
        elif choice == "4":
            self.destroy()
        else:
            messagebox.showinfo("Error", "Invalid choice. Please enter a valid option.")

    def register_customer(self):
        name = self.show_input_dialog("Enter Customer Name:")
        address = self.show_input_dialog('Enter Customer Address: ')
        contact_number = self.show_input_dialog("Enter Customer Contact Number: ")

        customer_obj = Customer(name, address, contact_number)
        self.customer_list.append(customer_obj)
        self.bank.add_customer(customer_obj)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Customer Registration:\n")
        self.output_text.insert(tk.END, f"Customer {name} registered successfully.\n")

    def existing_customer(self):
        account_number_input = self.show_input_dialog("Enter your account number: ")
        account_to_transact = self.bank.find_account_by_number(account_number_input)

        if account_to_transact:
            self.current_account = account_to_transact
            self.display_account_info()
        else:
            messagebox.showinfo("Error", "Account not found.")

    def display_customers_info(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, self.bank.display_bank_info())

    def display_account_info(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"\nWelcome, {self.current_account.owner.name}!\n")
        self.output_text.insert(tk.END, str(self.current_account) + "\n")

        while True:
            option = simpledialog.askstring("Options", "1. Enter 1 to deposit\n2. Enter 2 to Withdraw\n3. Enter 3 to Check the Balance\n4. Exit\n")

            if not option:
                break

            if option == "1":
                deposit_amount = int(self.show_input_dialog("Enter the amount to deposit: INR "))
                self.output_text.insert(tk.END, self.current_account.deposit(deposit_amount) + "\n")
            elif option == "2":
                withdrawal_amount = int(self.show_input_dialog("Enter the amount to withdraw: INR "))
                self.output_text.insert(tk.END, self.current_account.withdraw(withdrawal_amount) + "\n")
            elif option == "3":
                self.output_text.insert(tk.END, f"\nUpdated Account Information:\n{str(self.current_account)}\n")
            elif option == "4":
                break
            else:
                self.output_text.insert(tk.END, "Invalid Option\n")

        self.output_text.insert(tk.END, "\nOptions:\n1. Enter 1 to deposit\n2. Enter 2 to Withdraw\n3. Enter 3 to Check the Balance\n4. Exit\n")


    def show_input_dialog(self, message):
        return simpledialog.askstring("Input", message)

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
