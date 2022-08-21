"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

# i researched how to calculate primes, this may not be the best way and i might change underway but for now i will be trying to
# implement the Sieve of Eratosthenes. 

import time # because i wanted to time the algorithm

def SieveOfEratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2

    while p * p <= n:
        
        if primes[p] == True:

            for i in range(p**2, n+1, p):
                primes[i] = False

        p += 1

    primes[0] = False
    primes[1] = False

    print("Primes Computed, Preparing Output...")

    fprimes = []
    for p in range(n+1):
        if primes[p]:
            fprimes.append(p)

    return fprimes

if __name__ == "__main__":
    n = int(input("Input an integer you want to calculate all the primes up to: "))
    pOutput = input("Would you like the primes outputted? [y] or [n]: ")
    start_time = time.time()
    primes = SieveOfEratosthenes(n)
    #print(f"Following are the prime numbers smaller than or equal to {n}:\n",primes)
    if pOutput == "y":
        print(primes)
    print(f"There are {len(primes)} primes under {n}")
    print("--- %s seconds ---" % (time.time()-start_time))
    