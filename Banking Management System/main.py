"""
==========================================================
            BANK MANAGEMENT SYSTEM
==========================================================
Project Name : Bank Management System
Language     : Python
Storage      : JSON
Author       : Awais Raza
==========================================================
"""

import json
import os

Customers = {}

DATA_FILE = "bank_data.json"

ADMIN_USERNAME = "awais123"
ADMIN_PASSWORD = "awais@123"

class Customer:

    def __init__(self):
        self.name = ""
        self.account_no = ""
        self.username = ""
        self.password = ""
        self.email = ""
        self.phone_no = ""
        self.balance = 0.0

    def create_account(self, name,account_no, username, password, email, phone_no, balance):
        self.name = name
        self.account_no = account_no
        self.username = username
        self.password = password
        self.email = email
        self.phone_no = phone_no
        self.balance = balance
        print("Account created successfully.")
        

    def view_account(self):
        print("\n==========Account Details==========\n")
        print("Name:               ", self.name)
        print("Account Number:     ", self.account_no)
        print("Email:              ", self.email)
        print("Phone Number:       ", self.phone_no)
        print("Balance:            ", self.balance)
        print("\n===================================\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
            print("New Balance:", self.balance)
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance:", self.balance)

    def change_password(self):
        old_password = input("Enter old password: ")
        if old_password == self.password:
            new_password = input("Enter new password: ")
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Wrong old password.")

    def update_account(self):
        print("1. Update Email")
        print("2. Update Phone Number")
        choice = int(input("Enter choice: "))
        if choice == 1:
            self.email = input("Enter new email: ")
            print("Email updated.")
        elif choice == 2:
            self.phone_no = input("Enter new phone number: ")
            print("Phone updated.")
        else:
            print("Invalid choice.")    


        
class Bank:
    def __init__(self):
        pass

    def add_customer(self, name,account_no, username, password, email, phone_no, balance):

        if account_no in Customers:
            print("Account already Exists")
            return
        customer = Customer()
        if balance < 0:
            print("Invalid amount")
            return
        customer.create_account(name,account_no, username, password, email, phone_no, balance)

        Customers[account_no] = customer
        self.save_accounts()

        

    def search_customer(self):
        account_no = input("Enter account number:  ")

        if account_no in Customers:
            customer = Customers[account_no]
            customer.view_account()
        else:
            print("Account not found.")


    def admin_login(self):
        username = input("Enter username:  ")
        password = input("Enter password:  ")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            while True:
                print("\n==========ADMIN MENU==========")
                print("1. Add customer")
                print("2. Search customer")
                print("3. Display all accounts")
                print("4. Logout")
                choice = int(input("Enter choice:  "))
                if choice == 1:
                    name = input("Enter name:  ")
                    account_no = input("Enter account number:  ")
                    customer_username = input("Enter username:  ")
                    customer_password = input("Enter password:  ")
                    email = input("Enter email:  ")
                    phone_no = input("Enter phone number:  ")
                    balance = float(input("Enter initial balance:  "))

                    self.add_customer(name, account_no, customer_username, customer_password, email, phone_no, balance)

                elif choice == 2:
                    self.search_customer()
                elif choice == 3:
                    self.display_all_accounts()
                elif choice == 4:
                    print("----------LOGGED OUT----------")
                    break
                else:
                    print("Invalid choice.")

        else:
            print("Incorrect username or password.")

    def customer_login(self):
        username = input("Enter username:  ")
        password = input("Enter password:  ")

        for account_no, customer in Customers.items():
            if customer.username == username and customer.password == password:
                print("Login Successful")
                customer.view_account()
                self.customer_menu(customer)
                return customer
        print("Incorrect username or password.")
        return None

    def customer_menu(self, customer):

        while True:

            print("\n========== CUSTOMER MENU ==========")
            print("1. View Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Update Account")
            print("5. Change Password")
            print("6. Logout")
            print("===================================")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                customer.view_account()
            elif choice == 2:
                amount = float(input("Enter deposit amount: "))

                customer.deposit(amount)
                self.save_accounts()
            elif choice == 3:
                amount = float(input("Enter withdrawal amount: "))

                customer.withdraw(amount)
                self.save_accounts()
            elif choice == 4:
                customer.update_account()
                self.save_accounts()
            elif choice == 5:
                customer.change_password()
                self.save_accounts()
            elif choice == 6:
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice.")

    def display_all_accounts(self):
        if len(Customers) == 0:
            print("No accounts available.")
            return
        
        for account_no, customer in Customers.items():
            customer.view_account()


    def save_accounts(self):
        data = {}
        for account_no, customer in Customers.items():
            data[account_no] = {
                "name" : customer.name,
                "account_no" : customer.account_no,
                "username" : customer.username,
                "password" : customer.password,
                "email" : customer.email,
                "phone_no" : customer.phone_no,
                "balance" : customer.balance
            }
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully!!!")

    def load_accounts(self):
        if not os.path.exists(DATA_FILE):
            print("No previous data found.")
            return

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        for account_no, details in data.items():
            customer = Customer()
            customer.name = details["name"]
            customer.account_no = details["account_no"]
            customer.username = details["username"]
            customer.password = details["password"]
            customer.email = details["email"]
            customer.phone_no = details["phone_no"]
            customer.balance = details["balance"]

            Customers[account_no] = customer

        print("Data loaded successfully.")

def main():
    bank = Bank()

    bank.load_accounts()

    while True:
        print("==========================================================")
        print("                 BANK MANAGEMENT SYSTEM")
        print("==========================================================")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        print("==========================================================\n")

        choice = int(input("Enter your choice:  "))

        if choice == 1:
            bank.admin_login()
        elif choice == 2:
            customer = bank.customer_login()
            if customer is None:
                continue
        elif choice == 3:
            print("\n==========================================================")
            print("        Thank you for using BANK MANAGEMENT SYSTEM.")
            print("==========================================================\n")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()