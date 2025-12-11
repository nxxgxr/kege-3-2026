from itertools import *

alph=sorted('котбус')
cnt=0
for val in product(alph,repeat=8):
    val=''.join(val)
    if val.count('кот') >=1 and val[0] not in 'оу':
        cnt+=1

print(cnt)
