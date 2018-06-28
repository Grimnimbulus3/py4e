import re
hand = open('regex_sum_92023.txt')
numlist = list()
for line in hand:
    line=line.rstrip()
    stuff = re.findall('([0-9]+)',line)
    if len(stuff) == 0 : continue
    print(stuff)
    for things in stuff:
        num = float(things)
        numlist.append(num)
print(numlist)
numlist_sum = sum(numlist)
print(numlist_sum)
