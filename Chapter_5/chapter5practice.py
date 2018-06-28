Rawstr = input('Enter a number:')
try:
    Ival = int(Rawstr)
except:
    Ival = -1
if Ival>0:
    StrPlsOne = Ival+1
    print('One plus equals')
    print(StrPlsOne)
    print('Nice Work')
elif Ival==0:
    print('You entered zero')
else:
    print('Not a number')
