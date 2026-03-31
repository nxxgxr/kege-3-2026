from string import printable
from itertools import *
alph=printable[:25]
cnt=0
for val in product(alph,repeat=4):
    val=''.join(val)
    if val[0]!='0':
        kolvo=0
        count = 0
        for i in val:
            if i in printable[0:25:2]:
                kolvo+=1
            if i in printable[16:25]:
                count += 1
        if kolvo>=1 and count>2:cnt+=1


print(cnt)

