from itertools import *
from string import printable
cnt=0
alph=printable[:7]
for val in product(alph,repeat=6):
    val=''.join(val)
    if val[0]!='0':
        cntCh=0
        cntNe=0
        for i in range(6):
            if int(val[i],7) % 2 == 0:
                cntCh+=1
            else:
                cntNe+=1
        if cntCh==cntNe:
            if val[-1] not in '0123':
                    cnt+=1
print(cnt)

