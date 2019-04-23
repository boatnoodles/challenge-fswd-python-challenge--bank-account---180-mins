import datetime
import random


class Bank():
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_num] = account


class BankAccount():
    interest_rate = 0.056

    def __init__(self, name):
        self.acc_num = random.randint(1, 999999)
        self.balance = 0
        self.acc_owner = name
        self.acc_creation = datetime.datetime.now()

    def deposit_money(self, amount):
        self.balance += int(amount)

    def withdraw_money(self, amount):
        self.balance -= int(amount)

    def check_interest(self, time):
        return self.balance * (1 + self.interest_rate) ** time - self.balance

    def __str__(self):
        return f"New account by {self.acc_owner} with account number {self.acc_num:010d} has been created on {self.acc_creation}.\n"


class Money():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "RM{0:.2f}".format(self.value)


def print_error(error_msg):
    print(
        f"---------------------------------------------------------\nSorry we did not recognise that {error_msg}. Please try again.\n---------------------------------------------------------\n")


def print_balance(user_balance):
    print(
        f"---------------------------------------------------------\nYour balance is now {user_balance}.\n---------------------------------------------------------\n")


# Sets up a bank
ezpz_bank = Bank("EZPZ")


def main():

    while True:
        user_choice = input(
            "====================\nWelcome to EZPZ Bank\n====================\n1. Open a new account\n2. Check an existing account\n3. Exit\nWhat transaction would you like to perform today? ")

        second = True
        if user_choice == "1":
            #  Opens a new account
            user_name = input(
                "\nWhat will be the name of the account holder? ")
            amount_to_deposit = input(
                "How much would you like to deposit today? RM")
            try:
                new_account = BankAccount(user_name)
                new_account.deposit_money(amount_to_deposit)
                ezpz_bank.add_account(new_account)
                print(new_account)
            except:
                print_error("command")

        elif user_choice == "2":
            # Checks for an existing account
            user_num = input("\nWhat is your account number? ")
            # If account is found, use it as a key to obtain the corresponding account
            try:
                user_account = ezpz_bank.accounts[int(user_num)]
                # Ask user what transaction they would like to perform
                print(
                    f"---------------------------------------------------------\nWelcome back {user_account.acc_owner}.\n---------------------------------------------------------\n")
                while second == True:
                    user_choice_1 = input(
                        "1. Check account balance\n2. Deposit money\n3. Withdraw money\n4. Check interest earned so far\n5. Return to main menu\nWhat transaction would you like to perform today? ")

                    if user_choice_1 == "1":
                        # Checks account balance
                        user_balance = Money(user_account.balance)
                        print_balance(user_balance)

                    elif user_choice_1 == "2":
                        # Deposits money
                        dep_amount = input(
                            "How much would you like to deposit today? RM")
                        try:
                            user_account.deposit_money(dep_amount)
                            user_balance = Money(user_account.balance)
                            print_balance(user_balance)
                        except:
                            print_error("command")

                    elif user_choice_1 == "3":
                        # Withdraws money
                        wd_amount = input(
                            "How much would you like to withdraw today? RM")
                        try:
                            user_balance = user_account.balance
                            wd_amount = int(wd_amount)

                            if user_balance >= wd_amount:
                                # Only allow withdrawal up to user's balance
                                user_account.withdraw_money(wd_amount)
                                user_balance = Money(user_account.balance)
                                print_balance(user_balance)
                            else:
                                user_balance = Money(user_account.balance)
                                print(
                                    f"Insufficient balance. You only have {user_balance}.")
                        except:
                            print_error("command")

                    elif user_choice_1 == "4":
                        # Checks interest earned
                        time_duration = input(
                            "Enter the time period (years): ")
                        try:
                            total_interest = Money(
                                user_account.check_interest(int(time_duration)))
                            print(
                                f"---------------------------------------------------------\nYou have earned {total_interest} so far.\n---------------------------------------------------------\n")
                        except:
                            print_error("command")

                    elif user_choice_1 == "5":
                        # Returns to the main menu
                        second = False

                    else:
                        print_error("command")

            except KeyError:
                # Informs user if user is not found
                print_error("user")
            except:
                print_error("command")

        elif user_choice == "3":
            # Exits programme
            return False

        else:
            print_error("command")


main()
