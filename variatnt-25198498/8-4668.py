from itertools import *
from string import printable
alph=printable[:7]
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    if val[0] not in'0135' and val[-1] in '3456' and val.count('4')<=1:
        cnt+=1
        print(val)
print(cnt)