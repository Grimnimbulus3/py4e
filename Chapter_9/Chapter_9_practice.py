# a collection has more than 1 thing in it
# dictionaries are Python's most powerful data collections
#allow us to do fast database type operations
eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])#'dos'
len(eng2sp)#3
print('one' in eng2sp) #True
print('uno' in eng2sp) #false
vals = list(eng2sp.values())
print('uno' in vals) # True
#
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
purse['candy'] = purse['candy'] + 2
print(purse)
#
jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)
#many counters with a dictioanry
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen']+1
print(ccc)
#IT's an ERROR to reference a key that isn't in the dictionary, can GUARD w/ 'csev' in ccc
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names :
    if name not in counts:
        count[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)
#get() method simplifies this, adding ina key wityh a default if it isn't already in the dictionary
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
#count words ina afile
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('[Counts',counts)
#definite loops with dictionaries loops through keys, not values
#reteieving lists of keys and values
jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}
print(list(jjj)) # ['jan','chuck','fred']
print(jjj.keys()) # ['jan','chuck','fred']
print(jjj.values()) # ['jan','chuck','fred']
print(jjj.items()) # [('jan',100), ('chuck',1), ('fred',42)]  #TUPLES!
for aaa,bbb in jjj.itmes():
    print(aaa,bbb)
#find the most used word in a file
name = input('Enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        count[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
