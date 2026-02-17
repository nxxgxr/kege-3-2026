from itertools import product
from string import printable
cnt=0
alph=printable[:10]
for val in product(alph,repeat=4):
    val=''.join(val)
    if val[0]!='0':
        if val.count(val[0]) == val.count(val[1]) and val.count(val[2]) and val.count(val[3]) ==1:
            for i in range(0,10,2):
                val=val.replace(str(i),'*')
            for i in range(1,10,2):
                val=val.replace(str(i),'@')
            if '**' not in val and '@@' not in val:
                cnt+=1
print(cnt)