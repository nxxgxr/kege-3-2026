from itertools import *
from string import printable
cnt=0
alph=printable[:9]
for val in product(alph,repeat=5):
    val=''.join(val)
    if val[0] not in '0':
        if val.count('0')==1:
            for i in range(1,10,2):
                val=val.replace(str(i),'*')
            if '0*' not in val and '*0' not in val:
                cnt+=1
print(cnt)