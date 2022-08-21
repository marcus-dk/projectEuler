"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import time # because i wanted to time the algorithm

def SOESumOfPrimes(n):
    primes = [True for i in range(n+1)]
    p = 2

    while p * p <= n:
        
        if primes[p] == True:

            for i in range(p**2, n+1, p):
                primes[i] = False

        p += 1

    primes[0] = False
    primes[1] = False

    sum = 0
    for p in range(n+1):
        if primes[p]:
            sum += p

    return sum

if __name__ == "__main__":
    start_time = time.time()
    n = 2000000
    sum = SOESumOfPrimes(n)
    print(f"The sum of all primes below {n} is: {sum}")
    print("--- %s seconds ---" % (time.time()-start_time))
    