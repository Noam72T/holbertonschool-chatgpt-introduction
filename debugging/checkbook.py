class Checkbook:
    """
    A class to simulate a simple checkbook for managing deposits, withdrawals, and balance inquiries.

    Attributes:
        balance (float): Represents the current balance in the checkbook.

    Methods:
        deposit(amount):
            Adds a specified amount to the checkbook balance.
            Prints the deposited amount and the updated balance.

        withdraw(amount):
            Deducts a specified amount from the checkbook balance if sufficient funds are available.
            Prints the withdrawn amount and the updated balance. If insufficient funds, prints an error message.

        get_balance():
            Displays the current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes the Checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the balance.

        Parameters:
            amount (float): The amount to deposit into the checkbook.

        Side Effects:
            Updates the `balance` attribute and prints the deposit details.

        Example:
            cb.deposit(100.50)  # Adds $100.50 to the balance and displays the updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts a specified amount from the balance if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw from the checkbook.

        Side Effects:
            Updates the `balance` attribute if the withdrawal is successful.
            Prints the withdrawal details or an error message if there are insufficient funds.

        Example:
            cb.withdraw(50.00)  # Deducts $50.00 from the balance if funds are available.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance in the checkbook.

        Example:
            cb.get_balance()  # Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to run the interactive checkbook program.

    Prompts the user for actions: deposit, withdraw, balance, or exit.
    Based on the user input, performs the corresponding action:
    - 'deposit': Asks for an amount and adds it to the balance.
    - 'withdraw': Asks for an amount and deducts it from the balance if sufficient funds are available.
    - 'balance': Displays the current balance.
    - 'exit': Ends the program.

    Validates user input for proper commands and amounts.

    Example Usage:
        - deposit: Enter the amount to deposit.
        - withdraw: Enter the amount to withdraw.
        - balance: Check the current balance.
        - exit: End the program.

    Errors:
        - Prints an error message for invalid commands.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
