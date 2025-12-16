from itertools import *

alph=sorted('гранит')
cnt=0
for val in product(alph,repeat=6):
    val=''.join(val)
    cnt+=1
    if cnt%2==1 and val[0] not in 'аиг' and val.count('а') == 1:
        print(cnt)
        print(val)
        break

