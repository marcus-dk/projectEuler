"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

if __name__ == "__main__":
    number = 2 ** 1000
    sum = 0
    for i in str(number):
        sum += int(i)
    print(f"The sum of the digits of 2^1000 is: {sum}")

    