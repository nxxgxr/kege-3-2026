from itertools import *

alph = sorted('сублимаця')
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    cnt+=1
    if cnt%2 ==1 and val[-1] != 'я' and (val.count('у')+val.count('и')+val.count('а')+val.count('я')) ==2:
        print(cnt)
