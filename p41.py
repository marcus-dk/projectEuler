"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

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

def pandigitalCheck(num):
    strnum = str(num)
    digits = ['1', '2', '3', '4', '5', '6', '0']
    strnum = strnum.split()
    for i in strnum:
        if i in digits:
            digits = digits.pop(digits.index(i))

    if digits == []:
        return num
    else: 
        return False

    

if __name__ == "__main__":
    primes = soe(6543210)
    for i in primes[::-1]:
        result = pandigitalCheck(i)
        if result != False:
            print(f"{i} is the largest pandigital prime")
        
