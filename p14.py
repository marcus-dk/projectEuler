"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import time
start=time.time()
has2={}

def collatz(x):
    count = 1
    temp = x  
    while temp > 1:
        if temp % 2 == 0:
            temp = int(temp/2)
            if temp in has2:  # calculate temp and check if in cache
                count += has2[temp]
                break
            else:
                count += 1
        else:
            temp = 3*temp + 1
            if temp in has2:            
                count += has2[temp]
                break
            else:
                count += 1
        

    has2[x] = count
    return count

if __name__ == "__main__":
    num=0
    greatest=0
    for i in range(1000000):
        c=collatz(i)
        if num<c:
            num=c
            greatest=i
    print(f"{greatest} has {num} elements. calculation time = {time.time()-start} seconds.")