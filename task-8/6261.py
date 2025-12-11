from itertools import *
from string import printable
cnt=0
for val in product(printable[:8],repeat = 10):
    val=''.join(val)
    for i in range(len(val)-1):
        if int(val[i]) % 2 == 1 and val[i+1] == '7':
            break
    else:
        if val.count('7') == 5 and val[0]=='0' :
            cnt+=1


print(cnt)