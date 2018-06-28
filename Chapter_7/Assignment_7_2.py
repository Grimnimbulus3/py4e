# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print(line)
#print("Done")

fname = input('Enter file name: ')
fh = open(fname)
rum1 = 0
count1 = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    else:
        pos1 = line.find(':')
        str1 = line[pos1+1:]
        str2 = str1.lstrip()
        #print(str2)
        num1 = float(str2)
        rum1 = rum1 + num1
        count1 = count1 + 1
        #print(sum1, count1)
print('Average spam confidence:', rum1/count1)
