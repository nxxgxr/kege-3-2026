from itertools import *
from string import printable
alph=printable[:7]
cnt=0
for val in product(alph,repeat=7):
    val=''.join(val)
    if (val.count('0') + val.count('2') +val.count('4') +val.count('6')) == 2 and val[0] != '0':
        cnt+=1
print(cnt)