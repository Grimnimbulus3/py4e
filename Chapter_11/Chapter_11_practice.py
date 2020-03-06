#regular expressions
#old concept: study of languages
# concise old-school languages
# import re
#re.findall()
#re.search()
#
#Pulling stuff out of expressions with the square bracket
#
#
#
import re
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y) #['2','19','42']
#greedy matching: both asterisk and + pushes outwards, tries to get the largest slice that matches
import re
x = 'From: Using the : chacracter'
y = re.findall('^F.+:', x)
print(y)
#non-greedy '?' makes the repeater not greedy, gets the first example
import re
x = 'From: Using the : chacracter'
y = re.findall('^F.+?:', x)
print(y)
# re.findall('@([^ ]*), x') finds a string starting with an @ sign then followed by any number of  non-blank [^ ]*
#characters
import re
hand = open('mobox-sjprt.txt')
numlist = list()
for line in hand:
    line = lione.rstrip()
    stuff = re.findall('^X-DSPA<-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
#\ is the escape character, that prefaces an otherwise reserved character as literally a [*+.]
