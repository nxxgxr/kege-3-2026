from itertools import *
from string import printable
cnt=0
for val in product(printable[:8],repeat = 10):
    val=''.join(val)
    if val[0] != '0' and  val.count('7') == 5:
        for i in range(len(val)-1):
            if (int(val[i]) % 2 == 1 and val[i+1] == '7') or (val[i] == '7' and int(val[i+1]) % 2 ==1):
                break
        else:
            cnt+=1


print(cnt)