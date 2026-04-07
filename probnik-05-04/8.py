from string import printable
from itertools import *
alph=printable[:7]
cnt=0
for val in product(alph,repeat=7):
    val=''.join(val)
    if val[0] not in '035':
        if val.count('22')==0 or val.count('44')==0:
            cnt+=1
print(cnt)