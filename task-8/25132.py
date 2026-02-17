from itertools import *
alph=sorted('сдайегэ')
cnt=0
ans=0
for val in product(alph,repeat=6):
    val=''.join(val)
    cnt+=1
    if 'егэ' in val:
        ans+=cnt
print(ans)