from itertools import*
from string import printable as alph, printable
cnt=0
for val in product(printable[:16],repeat=3):
    val=''.join(val)
    if val[0] != '0' and len(set(val)) :
        cnt+=1
print(cnt)
