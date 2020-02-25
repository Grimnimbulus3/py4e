#original
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #iprint 'Debug:', words
    if len(words) ==0: continue
    if words[0] != 'From': continue
    print(words[2])
#new combined if statement
print('new version')
fhand = open('C:\\Users\\i20554.MARKETSTANCE\\github\\py4e\\Sample_Data\\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #iprint 'Debug:', words
    if len(words) !=0 and words[0] == 'From':
         print(words[2])
    else: continue
