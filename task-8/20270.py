from itertools import *
from string import printable
alph=printable[:7]
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    if val[0]!='0':
        for i in range(0,8,2):
            val=val.replace(str(i),'*')
        for i in range(1,8,2):
            val = val.replace(str(i), '!')
        chet=val.count('**')
        if chet>1:
            if '***' not in val:
                cnt+=1
                print(val)
print(cnt)