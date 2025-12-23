from itertools import *
alph=sorted('мизантроп')
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    cnt+=1
    if val[0]!=0 and cnt%2==0 and val[0]=='н' and val.count('р')==2:
        print(cnt)