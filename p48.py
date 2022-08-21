"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

"""

def selfPowers():
    sum = 0
    for i in range(1,1001):
        sum += i**i

    return sum


if __name__ == "__main__":
    ans = selfPowers()
    print(ans)
    print(str(ans)[-10:-1]+str(ans)[-1])
