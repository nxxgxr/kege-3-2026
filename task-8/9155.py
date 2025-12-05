from itertools import *

alph=sorted('апрель')[::-1]
cnt=0
ans=0
for val in product(alph,repeat=6):
    cnt+=1
    slovo=''.join(val)
    if slovo[-1] == 'ь' and cnt < 388:
        ans+=1
print(ans)
