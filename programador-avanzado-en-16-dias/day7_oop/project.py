import os
import pickle
from random import choice


# Person class with name and last name
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


# Client class with account_number and balance
class Customer(Person):
    def __init__(self, name, last_name, account_number, balance):
        super().__init__(name, last_name)
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Your balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposit ${amount} to your account")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"You have withdraw ${amount} from your account")

    def __str__(self):
        information = (
            f"Name: {self.name}\n"
            + f"Last_name: {self.last_name}\n"
            + f"Account number: {self.account_number}\n"
            + f"Balance: {self.balance}\n"
        )
        return information


def read_customers():
    # Load the instance back from the .pkl file
    with open("pkls/customers.pkl", "rb") as f:
        customers = pickle.load(f)

    return customers


def write_customer(customer):
    customers = read_customers()
    customers.append(customer)
    update_customers(customers)


def deposit_amount(account_number, amount):
    customers = read_customers()
    for customer in customers:
        if str(customer.account_number) == account_number:
            customer.deposit(amount)
            break

    update_customers(customers)


def withdraw_amount(account_number, amount):
    customers = read_customers()
    for customer in customers:
        if str(customer.account_number) == account_number:
            customer.withdraw(amount)
    update_customers(customers)


def update_customers(customers):
    with open("pkls/customers.pkl", "wb") as f:
        pickle.dump(customers, f)


def read_account_numbers():
    # Load the instance back from the .pkl file
    with open("pkls/customer_account_numbers.pkl", "rb") as f:
        customer_account_numbers = pickle.load(f)

    return customer_account_numbers


def create_account_number():
    # Read available account numbers
    account_numbers = read_account_numbers()

    # Select a random account number
    account_number = choice(account_numbers)

    # Remove selected account number from the list of avaiable account numbers
    account_numbers.remove(account_number)
    update_account_numbers(account_numbers)

    # Return account_number
    return account_number


def update_account_numbers(account_numbers):
    with open("pkls/customer_account_numbers.pkl", "wb") as f:
        pickle.dump(account_numbers, f)


def create_customer():
    name = input("Write your first name: ")
    last_name = input("Write your last name: ")
    account_number = create_account_number()
    balance = 0
    customer = Customer(name, last_name, account_number, balance)
    write_customer(customer)
    return customer


def remove_customer(customer_account_number):
    customers = read_customers()
    customerer_account_numbers = read_account_numbers()
    if len(customers) != 0:
        for index, custom in enumerate(customers):
            if str(custom.account_number) == customer_account_number:
                customers.pop(index)
                customerer_account_numbers.append(customer_account_number)
                update_customers(customers)
                update_account_numbers(customerer_account_numbers)
                print(f"Customer {customer_account_number} was removed")
                return
        print(f"Customer {customer_account_number} was not found")
        return

    else:
        print("There are not customers to remove")
        return


def remove_customers():
    customers = read_customers()
    if len(customers) != 0:
        update_customers([])
        update_account_numbers(list(range(1, 101)))
        print(f"{len(customers)} customers were removed")
    else:
        print("There are not customers to remove")
        return


def customer_information(customer_account_number):
    customers = read_customers()
    information = ""
    if len(customers) != 0:
        for customer in customers:
            if str(customer.account_number) == customer_account_number:
                information += f"\n | Customer: {customer_account_number} |\n"
                information += str(customer)
                return information
        information = f"Customer {customer_account_number} was not found"
        return information
    else:
        information += "There are not customers"
        return information


def validate_client_existend(account_number):
    customers = read_customers()
    if len(customers) != 0:
        for customer in customers:
            if str(customer.account_number) == account_number:
                return True
        return False
    else:
        return False


def customer_informations():
    customers = read_customers()
    information = ""
    if len(customers) != 0:
        for custom in customers:
            information += f"\n | Customer {custom.account_number} |\n"
            information += str(custom)
    else:
        information += "There are not customers"

    return information


def display_options():
    print("1. Create customer\n" "2. Enter account\n" "3. Manager\n" "4. Get out\n")


def display_menu_options():
    print(
        "1. Deposite\n"
        "2. Withdraw\n"
        "3. Information\n"
        "4. Remove account\n"
        "5. Get out"
    )


def display_manager_menu_options():
    print("1. Information\n" "2. Remove all accounts\n" "3. Get out\n")


def select_clear():
    # Wait for the user to press enter
    input("Press Enter to continue...")
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")


# Acount modification


def start():
    option = 0
    while option != "4":
        display_options()
        option = input("What you want to do? ")
        match option:
            case "1":
                customer = create_customer()
                print(
                    f"Customer {customer.name} was added with {customer.account_number} account_number"
                )
                select_clear()

            case "2":
                account_number = input("Enter your account number: ")
                if validate_client_existend(account_number) == True:
                    # Clear the console
                    os.system("cls" if os.name == "nt" else "clear")
                    menu(account_number)
                else:
                    print("This account doesn't exist")
                    select_clear()
            case "3":
                manager_menu()
                select_clear()

            case "4":
                print("Get out")
                select_clear()
                break

            case _:
                print("that option doesn't exists")


def menu(account_number):
    option = 0
    while option != 5:
        display_menu_options()
        option = input("What you want to do? ")

        match option:
            case "1":
                amount = float(input("Enter a amount to deposit: "))
                deposit_amount(account_number, amount)
                select_clear()

            case "2":
                amount = float(input("Enter a amount to withdraw: "))
                withdraw_amount(account_number, amount)
                select_clear()

            case "3":
                print(customer_information(account_number))
                select_clear()

            case "4":
                remove_customer(account_number)
                select_clear()
                break

            case "5":
                break

            case _:
                print("This option doesn't exist")


def manager_menu():
    option = 0
    while option != 3:
        display_manager_menu_options()
        option = input("Enter a option: ")
        match option:
            case "1":
                print(customer_informations())
                select_clear()

            case "2":
                remove_customers()
                select_clear()

            case "3":
                break


# Main
start()
