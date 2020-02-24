#start by making a handle like so (give every \ two \\s)
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox.txt')
count = 0
for line in fhand:
    count = count+1
print('Line Count:', count)
shand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
#fhand.read reads the file, then prints the string's length, and it's first 20 characters
inp = shand.read()
print(len(inp))
print(inp[:20])
#rstrip() strips out whitespace
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#or continue skips a line that doesn't meet a condition in this example
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
#look for something in particular
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
#prompt for a file name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count+1
print('There were',count,'subject lines in', fname)
#deal with bad inputs
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count+1
print('There were',count,'subject lines in', fname)
