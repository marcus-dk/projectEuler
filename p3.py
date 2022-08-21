"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# i have decided to restart my design of the program using a function to test if a number is prime meaning i do not need to use a list of primes
# using a list of primes would be faster as i would not have to perform a check of every number however the list would need to contain enough primes to test for every
# possible prime factor.

num = 600851475143
primefactors = []

def findPrimeFactors(num,primefactors):
    
    n = 2
    
    while n * n < num: # Based on the concept that the largest prime factor will always be smaller than the square root of num

        while num % n == 0:
            primefactors.append(n)
            num /= n

        n += 1

    primefactors.append(int(num))
    return primefactors

if __name__ == "__main__":
    print(f"The prime factors of {num} is:",findPrimeFactors(num,primefactors))


# this was my original attempt but as it used a list of primes it was very flawed and was not able to solve the problem
"""
# this will not be an ideal solution to find the prime factors of all numbers as i'm as of right now not sure how i would implement a formula for it
# however this method should work for most numbers that arent obscenely large

# list of prime numbers 1 - 1000 (can be changed as wished) must be sorted from lowest to greatest
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 
461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

# number you wish to find the prime factors of
num = 600851475143

def findPrimeFactors(primes, num):

    done = False
    primefactors = []
    counter = 0
    try:
        while num != 1:
                if num % primes[counter] == 0:
                    primefactors.append(primes[counter])
                    num /= primes[counter]
                    continue
                else:
                    counter += 1
    except IndexError:
        print("An error occurred,",num,primefactors,counter)

    errorcheck = 1

    for i in primefactors:

        errorcheck *= i

    if errorcheck == num:
        print("The list of prime factors is as follows: ",", ".join(primefactors))
        
    else:
        print("The list of prime numbers provided does not contain enough primes to find all factors.")

if __name__ == "__main__":
    findPrimeFactors(primes, num)
"""