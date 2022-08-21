"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# most efficient solution should be to find all pythagorean triplets then find the one that adds up to 1000


def FindPythagoreanTriplets(limit):

    c,m = 0,2
    triplets = []

    while c < limit:
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            # if c is greater than
            # limit then break it
            if c > limit :
                break
 
            triplets.append([a,b,c])
 
        m += 1

    return triplets

def checkSums(lists, goal):

    for i in lists:

        temp = 0
        for num in i:
            temp += num

        if temp == goal:
            return i
            
    return False

if __name__ == "__main__":
    triplets = FindPythagoreanTriplets(limit=1000)
    goallist = checkSums(triplets,goal=1000)
    product = 1

    for i in goallist:
        product *= i

    print(f"The Product of the triplet you sought is {product}. The triplet was {goallist}")
