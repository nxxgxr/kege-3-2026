from itertools import *
from string import printable
alph=printable[:8]
cnt=0
for val in product(alph,repeat=6):
    val=''.join(val)
    if val[0]!='0' and len(val)==len(set(val)) and int(val,8) % 5 == 0:
        for i in range(0,8,2):
            val=val.replace(str(i),'*')
        for i in range(1,8,2):
            val=val.replace(str(i),'!')
        if '**' not in val and '!!' not in val:
            cnt+=1
print(cnt)
