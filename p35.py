"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

import time # because i wanted to time the algorithm

def CircularPrimesSOE(n):
    primes = [True for i in range(n+1)]
    p = 2

    while p * p <= n:
        
        if primes[p] == True:

            for i in range(p**2, n+1, p):
                primes[i] = False

        p += 1

    primes[0] = False
    primes[1] = False

    fprimes = []
    for p in range(n+1):
        if primes[p]:
            fprimes.append(p)

    for prime in fprimes:
        variations = []
        loopednum = str(prime)

        for i in range(len(loopednum)):
            loopednum += loopednum[0]
            loopednum = loopednum[1:]
            variations.append(int(loopednum))

        for variation in variations:
            if variation in fprimes:
                continue
            else:
                fprimes.pop(fprimes.index(prime))
                break
        
    return fprimes

if __name__ == "__main__":
    print("This code will take circa 3 minutes to run, if you want faster then don't fucking run it in python you nonce. Learn C++ headass")
    start_time = time.time()
    n = 1000000
    primes = CircularPrimesSOE(n)
    print(f"Following are the Circular prime numbers smaller than or equal to {n}:\n",primes)
    print(f"There are {len(primes)} circular primes below 1 million")
    print("--- %s seconds ---" % (time.time()-start_time))
    