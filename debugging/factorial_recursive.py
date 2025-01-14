#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`. If `n` is 0, returns 1 (as 0! = 1).

    Raises:
    RecursionError: If the recursion limit is exceeded.
    ValueError: If `n` is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main program execution
if __name__ == "__main__":
    """
    This section runs the script when executed directly.
    It reads a command-line argument, calculates its factorial,
    and prints the result.
    """
    try:
        # Parse the command-line argument as an integer
        number = int(sys.argv[1])
        
        # Calculate the factorial of the provided number
        result = factorial(number)
        
        # Print the result
        print(result)
    except IndexError:
        print("Error: No input provided. Please provide a non-negative integer.")
    except ValueError as e:
        print(f"Error: {e}")
    except RecursionError:
        print("Error: Recursion limit exceeded. The input is too large.")

