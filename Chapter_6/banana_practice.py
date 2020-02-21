fruit = 'banana'
letter = fruit[1]
print("Print(letter)")
print(letter) # should return a, since fruit[0] is b not fruit[1]
print("Returns a, since fruit[0] is b not fruit[1]")
length = len(fruit)
last = fruit[length-1]
print("Last:",last)
last = fruit[-1]
print("Last:",last)
# last in the previous 2 statements should be the same
print("last in the previous 2 statements should be the same")
#
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
#this next query gives an identical output to the previous
for char in fruit:
    print(char)
#now going to String slices
s = 'Monty Python'
print(s[0:5]) # Returns 'Monty'
print(s[6:12]) #Returns 'Python'
fruit = 'banana'
fruit[:3] # returns 'ban'
fruit[3:] # returns 'ana'
fruit[3:3] # returns ''
#
greeting = 'Hello, world!'
print(greeting)
#greeting[0] = 'J'   #doesn't make 'Jello, world!', becuase strings are immutable
new_greeting = 'J'+greeting[1:]
print(new_greeting)
#
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count+1
print(count) # returns a 3 because there are 3 a's in banana
#
'a' in 'banana' #returns True
'seed' in 'banana' #returns Flase
if word == 'banana':
    print('All right, bananas.')# returns 'All right, bananas.' because word==banana
#
if word < 'banana':
    print('Your word,'+word+', comes before banana.')
elif word>'banana':
    print('Your word,'+word+', comes after banana.')
else:
    print('All right, bananas.')
#
stuff = 'Hello World!'
type(stuff) #returns <class 'str'>
dir(stuff) #returns methods that can be used on strings
help(str.capitalize) #returns details on what the str.capitalize method does
#
word = 'banana'
new_word = word.upper()
print(new_word) # returns BANANA
index = word.find('a')
print(index) # returns 1, the location of the first a in bananas
word.find('na') # returns 2, the beginning of the first 'na' substring
word.find('na',3) # returns 4, the begining of the first 'na' substring starting at 4th letter of banana
line = ' Here we go '
line.strip() #returns 'Here we go', stripping out the leading and following whitespaces
line = 'Have a nice day'
line.startswith('Have') # returns True
line.startswith('h') #returns False, requires case to match
line.lower() #returns have a nice day
line.lower().startswith('h') #returns True, since startswith is executed on the lowered line
#
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos) #returns 21
sppos = data.find(' ',atpos)
print(sppos) #returns 31
host = data[atpos+1:sppos]
print(host) #returns uct.ac.za
#format operator
#%d is integer, %g ins floating point, %s is string
camels = 42
print('%d' % camels) # returns '42'
print('I have spotted %d camels.' % camels)
print('IN %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
