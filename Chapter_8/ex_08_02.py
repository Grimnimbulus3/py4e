#original
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #iprint 'Debug:', words
    if len(words) ==0: continue
    if words[0] != 'From': continue
    print(words[2])
# problem: print(words[2]) is still un gaurded from lines starting with from that don't have at least 3 parts
#fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short-guard.txt')
#count = 0
#for line in fhand:
    #words = line.split()
    #iprint 'Debug:', words
    #if len(words) ==0: continue
    #if words[0] != 'From': continue
    #print(words[2])
#solution: make it so that a third if checks for that
print('Try new script')
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short-guard.txt')
count = 0
for line in fhand:
    words = line.split()
    #iprint 'Debug:', words
    if len(words) ==0: continue
    if words[0] != 'From': continue
    if len(words)<3: continue
    print(words[2])
