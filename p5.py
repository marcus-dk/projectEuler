"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

# this puzzled me quite a lot in the beginning as to how i would efficiently be able to solve this problem
# after a bit of research as to how you can calculate 2 numbers' LCM i found a way that i understand and feel that i can easily implement

# was struggling to implement stuff the way i wanted, got help from the internet :(
# ended up finding a solution in java, optimised it a bit and then translated it to python


# code for specifically finding the lcm for numbers 1,20 

def isLCM(i):
    if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        return True

result = 1
i = 2520

while i > 0: 

    if isLCM(i) == True:

        result = i
        break

    i += 2520

print(result)