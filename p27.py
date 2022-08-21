"""
https://projecteuler.net/problem=27

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

n^2 + an + b, where |a| < 1000 and |b| _< 1000
"""

def soe(n): # Sieve of Eratosthenes Implementation in Python 3.7
    primalityFlags = [True]*(n+1) # List of Bool Values that will decide whether or not to run an iteration
    primalityFlags[0] = primalityFlags[1] = False # 0 and 1 aren't prime
    primes = [] # List that all primes will be appended to

    for i, flag in enumerate(primalityFlags): # enumerate adds an iterable object to each bool value in list
        if flag:
            primes.append(i) # appends prime

            for j in range(2*i, n+1, i): # changes bool values for all multiples of the prime
                primalityFlags[j] = False

    return primes

def nthprimes(primes, a, b):
    count = 0
    for i in range(0,100):
        calc = i**2 + i*a + b
        if calc in primes:
            count += 1
            continue
        else:
            til = i-1
            break
    
    return [count, a, b, til]

    pass

def main():
    primes = soe(100000)
    mostprimes = [0, 0, 0, 0] # list [count of consecutive primes, a, b, number it produces primes to] with the values that produced the most primes
    a = 0
    b = 0

    for i in range(0, 1000):
        a += 1
        for i in range(0, 1001):
            b += 1
            nth = nthprimes(primes, a, b)
            
            if mostprimes[0] < nth[0]:
                mostprimes = [nth[0], a, b, nth[1]]
    
    print(f"The formula that will produce the most consecutive primes is n^2 + {mostprime[1]}n + {mostprimes[2]}\nThis formula produces primes from 0<=n<={mostprimes[3]}.")


if __name__ == "__main__":
    main()



