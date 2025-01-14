#!/usr/bin/python3

class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance inquiries.

    Attributes:
        balance (float): The current balance of the checkbook.
    """
    def __init__(self):
        """
        Initialize a Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit an amount into the checkbook.

        Parameters:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw an amount from the checkbook.

        Parameters:
            amount (float): The amount to be withdrawn.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook. Provides options to deposit,
    withdraw, check balance, or exit the application.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

