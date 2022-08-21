"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def sumofFactorialDigits(num):
    
    factnum = 1
    for i in range(1,num+1):
        factnum *= i
    
    factsum = 0
    for i in str(factnum):
        factsum += int(i)

    return [factsum, factnum]


if __name__ == "__main__":
    ans = sumofFactorialDigits(100)
    print(ans[1])
    print(f"The sum of the digits of the number 100! is: {ans[0]}")
    