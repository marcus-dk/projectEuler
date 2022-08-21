"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

wordnums = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eightteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

if __name__ == "__main__":
    charsto1000 = 0
    for i in range(1001):
        x = i
        if x >= 100:
            charsto1000 += len(wordnums[x]+"hundred")
            x -= int(str(x)[0])*100
        if str(x)[0] == "1": 
            charsto1000 += len(wordnums[x])
            x -= int(wordnums[x])
        elif len(str(x)) < 1:
            y = str(x)
            print(y)
            print(y [0])
            y = y[0] + "0"
            print(y)
            charsto1000 += len(wordnums[y])
            x -= int(y)
        if x != 0:
            charsto1000 += len(wordnums[x])
            x -= x





