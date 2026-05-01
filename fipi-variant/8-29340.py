from itertools import *
alph=sorted('апрель')
cnt=0
for val in product(alph,repeat=6):
    val=''.join(val)
    cnt+=1
    if val[0] not in 'ал' and val.count('п') >=2:
        if cnt%2 ==1:
            print(cnt)
            break