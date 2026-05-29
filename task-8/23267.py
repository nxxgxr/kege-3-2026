from itertools import *
alph=sorted('строка')
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    cnt+=1
    if cnt%2==1 and val[0] not in 'ал' and val.count('с')==1:
        print(cnt)