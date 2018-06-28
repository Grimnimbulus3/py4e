name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    #print(time)
    time_split = time.split(':')
    #print(time_split)
    hour = time_split[0]
    #print(hour)
    #for hours in hour:
        #counts[hours] = counts.get(hours, 0) + 1
    counts[hour] = counts.get(hour, 0) + 1

counts_list = counts.items()
#print(counts_list)

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)
for(a,b) in (lst):
    print(a,b)


#print(lst)
