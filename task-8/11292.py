from itertools import product
from string import printable
alph=printable[:16]
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    if val[0]!='0':
        if val.count('6')==2:
            val=val.replace('6',"&")
            for i in range(0,17,2):
                val=val.replace(str(i),'*')
                if '*&' not in val and '&*' not in val:
                    cnt+=1

print(cnt)
