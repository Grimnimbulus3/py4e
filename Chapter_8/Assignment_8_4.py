#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#print(line.rstrip())

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
