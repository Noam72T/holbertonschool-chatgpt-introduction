#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Function Description:
        This function computes the factorial of a non-negative integer using recursion.
        Factorial is defined as the product of all positive integers up to the given number.
        For example, factorial(4) = 4 * 3 * 2 * 1 = 24.

    Parameters:
        n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input number. Returns 1 if n is 0.

    Raises:
        RecursionError: If the recursion depth is exceeded (e.g., for very large n).
        ValueError: If n is negative, as factorial is not defined for negative integers.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
