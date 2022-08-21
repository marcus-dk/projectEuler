"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from math import fabs # to get absolute value of difference

nums = 100

def SumOfSquares(nums):
    sos = 0

    for i in range(1,nums + 1):

        sos += i * i
    
    return sos

def SquareOfSum(nums):
    sos = 0

    for i in range(1,nums + 1):
        sos += i
    
    sos *= sos

    return sos

def main(nums):
    ans = int(fabs(SumOfSquares(nums) - SquareOfSum(nums)))
    print(f"The difference between the sum of the squares of the first one {nums} natural numbers and the square of the sum is,", ans)

if __name__ == "__main__":
    main(nums)