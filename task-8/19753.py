from itertools import *
from string import *
alph=printable[:10]
cnt=0
for val in product(alph,repeat=6):
    val=''.join(val)
    if val[0] != '0' and int(val) % 4 ==0:
        for i in range(len(val) - 1):
            if int(val[i]) % 2 == 0 and int(val[i + 1]) % 2 == 0:
                break
        else:
            for i in val:
                if val.count(i) > 1:
                    break
            else:
                cnt+=1

print(cnt)