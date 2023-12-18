"""
This module defines a solver function to find the smallest number evenly divisible
by all the numbers in the range from p to q.
"""


def solver(p, q):
    """
    Finds the smallest number evenly divisible by all the numbers in the range from p to q.
    """
    start = min(p, q)
    end = max(p, q)

    num = end

    while True:
        flag = True
        for i in range(start, end + 1):
            if num % i != 0:
                flag = False
                break

        if flag:
            return num

        num += 1


if __name__ == "__main__":
    print(f"{solver(1, 20)}")
