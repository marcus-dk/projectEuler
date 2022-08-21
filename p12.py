"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""

def calcTriNums(numoftrinums):
    # Gauss Bean Counting
    nums = []
    for i in range(numoftrinums+1):
        trinum = i * (i+1) // 2
        nums.append(trinum)
    return nums


def checkFactors(x, factors):
    # from internet

    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
        i += 1
    
    if len(result) >= factors:
        print(len(result))
        print(result)
        return True
    else:
        return False

if __name__ == "__main__":
    factors = 500
    numoftrinums = 100000
    trianglenumbers = calcTriNums(numoftrinums)
    for i in trianglenumbers:
        print(i)
        ans = checkFactors(i, factors)
        if ans == True:
            print(f"The first triangle number to have over five hundred divisors is: {i}")
            quit()
        
    
