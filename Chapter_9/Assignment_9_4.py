name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email,0) + 1

bigcount = None
bigemail = None
for email_1, count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email_1
        bigcount = count

print(bigemail, bigcount)
