from itertools import *
from string import *
alph=printable[:9]
cnt=0
for val in product(alph,repeat=4):
    val=''.join(val)
    if val[0]!='0':
        if val.count('8')==1:
            ind=val.index('8')
            cnt_do=0
            cnt_posle=0
            for i in val[:ind]:
                cnt_do+=int(i)
            for i in val[ind+1:]:
                cnt_posle+=int(i)
            if cnt_do==cnt_posle:
                cnt+=1

print(cnt)
