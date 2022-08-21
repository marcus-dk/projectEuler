"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# i will solve this by implementing a for loop in the range of 1000 (the range of numbers we are working with) and then use the modulus operator to determine
# whether or not a number is a multiple of 3 or 5. if it is i will add it to the sum, if not i will simply continue the loop.

sum = 0

for i in range(1000):

    if i % 3 == 0: 
        sum += i
        continue

    elif i % 5 == 0:
        sum += i
        continue

    else:
        continue
    
print("The sum of all natural numbers that are multiples of 3 or 5 below 1000 is",sum)