str = 'X-DSPAM-Confidence:    0.8475'
ppos=str.find('0')
sval = text[ppos:]
ival = float(sval)
print(ival)
