"""

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

def fibonacci_of(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci_of(n-1) + fibonacci_of(n-2)

if __name__ == "__main__":
    x = fibonacci_of(100)

    print(f"The first fibonacci number with a 1000 digits is {x} with an index of")
