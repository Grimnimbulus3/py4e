fname = input('Enter the file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    Inp_Upper = line.upper()
    print(Inp_Upper)
