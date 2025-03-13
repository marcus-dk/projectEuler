"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n == 1000:
        return "onethousand"
    
    words = []
    
    if n >= 100:
        words.append(ones[n // 100] + "hundred")
        if n % 100 != 0:
            words.append("and")
        n %= 100
    
    if n > 0:
        if n < 20:
            words.append(ones[n])
        else:
            words.append(tens[n // 10])
            if n % 10 != 0:
                words.append(ones[n % 10])
    
    return "".join(words)

def count_letters(n):
    total = 0
    
    for i in range(1, n + 1):
        words = number_to_words(i)
        letter_count = len(words)
        total += letter_count
        
    return total

if __name__ == "__main__":
    result = count_letters(1000)
    print(result)
    
