#Lists
#lists are collections
friends = [ 'Joseph', 'Glenn', 'Sally' ]
#list constants are anything in queare brackets
#lists don't have to be the same type of data
print(['red', 24, 98.6])
print([1, [5,6], 7])
print([])
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
#
friends = ['Joseph','Glenn','Sally']
print(friends[1]) #should return Glenn
#lists are mutable
lotto = [2, 14, 26, 41, 63]
print(lotto) #[2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto) #[2, 14, 28, 41, 63]
len(lotto) #5
#range functions
print(range(4)) #[0.1.2.3]
#
friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print ('Happy New Year:', friend)
#counted loop, going through a range of numbers
friends = ['Joseph','Glenn','Sally']
for i in range(len(friends)):
    friend = friends[i]
    print ('Happy New Year:', friend)
#adding lsits together
a = [1,2,3,]
b = [4,5,6]
c = a+b
print(c) #[1,2,3,4,5,6]
print(a) #[1,2,3]
#slicing Lists
t = [9, 41, 12, 3 ,74, 15]
t[1:3] #[41,12]
t[:4] #[9, 41, 12, 3]
#list methods
#building a list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)#['book',99]
stuff.append('cookie')
print(stuff)# ['book',99,'cookie']
#checking a list
some = [1,9,21,10,16]
9 in some #True
15 in some#false
20 not in some#True
#lists are in order, can be sorted
friends = ['Joseph','Glenn','Sally']
friends.sort()
print(friends) #['Glenn','Joseph','Sally']
#built in functions for lsits
nums = [3,41,12,9,74,15]
print(len(nums))#6
print(max(nums))#74
print(min(nums))#3
print(sum(nums))#154
print(sum(nums)/len(nums))#25.6
#list appending loop
numlist = list()
while True:
    inp = input('Enter a number(done when done): ')
    if inp == 'done' :
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:', average)
#lists and strings
abc = 'With three words'
stuff = abc.split()
print(stuff) #['With','three','words']
print(len(stuff))#3
print(stuff[0])#with
for w in stuff:
    print(w)
#split splits on spaces, but mutliple whitespaces count as 1 delimiter
#can also work on non-whitespaces
line  = 'first;second;third'
thing = line.split(';')
print(thing) #['first','second','third']
#parsing mail data example
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
#double splits
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])#uct.ac.za
#extending and deleting
t1 = ['a','b','c']
t2 = ['d','e']
t1.extend(t2)
print(t1) #[a','b','c','d','e']
x = t1.pop(1)
print(t1) #['a','c','d','e']
print(x) #'b'
del t1[1]
print(t1) #['a','d','e']
t1.remove('d')
print(t1) #['a','e']
t = ['a','b','c','d','e','f']
del t[1:5]
print(t) #['a','f']
#lists and strings
s='spam'
t = list(s)
print(t) # ['s','p','a','m']
#joining
s = 'pining for the fjords'
t = s.split()
print(t) #[pining','for','the','fjord']
delimiter = ' '
s = delimiter.join(t) #'pining for the fjords'
print(s)
