"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

from string import ascii_uppercase

ascii_u_list = list(ascii_uppercase)

file = open("p022_names.txt", "r")
filecontent = file.read()
names = filecontent.split(',')

for name in names:
    names[names.index(name)] = name.strip('"')

file.close()

names.sort()
namesvalue = []

for name in names:
    value = 0
    for letter in name:
        value += ascii_u_list.index(letter)+1
    value *= names.index(name)+1
    namesvalue.append(value)

sum = 0
for value in namesvalue:
    sum += value

print(sum)