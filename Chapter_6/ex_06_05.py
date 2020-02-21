str = 'X-DPSM-Confidence:0.8475'
colon_pos = str.find(':')
num = str[colon_pos+1:]
fnum = float(num)
print(fnum)
