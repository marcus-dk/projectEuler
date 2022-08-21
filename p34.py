"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

"""

from math import factorial

def findCuriousNums():

    curiousnums = []

    for num in range(3,100000):
        factSum = 0

        for i in str(num):
            factSum += factorial(int(i))
        
        if factSum == num:
            curiousnums.append(num)

    return curiousnums

if __name__ == "__main__":
    curiousnums = findCuriousNums()
    sum = 0
    for i in curiousnums:
        sum += i
    print(f"All curious numbers are: {curiousnums}")
    print(f"The sum of these curious numbers is: {sum}")