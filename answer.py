"""
This module imports the solver function and uses it to find the smallest number
evenly divisible by all the numbers in the range from 1 to 20.
"""
from solver import solver


def answer():
    """
    Calls the solver function to find the smallest number evenly divisible
    by all numbers in the range from 1 to 20.
    """
    return f"{solver(1,20)}"


if __name__ == "__main__":
    print(f"Smallest number is: {answer()}")
