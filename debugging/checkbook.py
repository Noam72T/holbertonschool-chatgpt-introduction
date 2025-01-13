class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance tracking.
    
    Attributes:
        balance (float): The current balance in the checkbook.
    """
    
    def __init__(self):
        """
        Initializes the checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the balance.

        Parameters:
            amount (float): The amount to deposit into the checkbook.
        
        Prints the deposited amount and the updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts a specified amount from the balance if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw from the checkbook.
        
        Prints the withdrawn amount and the updated balance, or informs the user
        if there are insufficient funds.
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
        
        Prints the current balance without making any changes to it.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interactively run the checkbook program.
    
    Prompts the user for actions (deposit, withdraw, balance, or exit) and executes
    the corresponding methods from the Checkbook class.
    Handles invalid inputs and ensures that the program doesn't crash.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = input("Enter the amount to deposit: $")
                amount = float(amount)  # Attempt to convert input to a float
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action.lower() == 'withdraw':
            try:
                amount = input("Enter the amount to withdraw: $")
                amount = float(amount)  # Attempt to convert input to a float
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
