from string import *
from itertools import *
alph=printable[:7]
cnt=0
for val in product(alph,repeat=5):
    val=''.join(val)
    if val[0] != '0':
        tri = val.count('3') +  val.count('4') + val.count('5')  == 2
        if tri:
            mq=True
            for i in range(len(val)-1):
                if val[i]==val[i+1]:
                    mq=False
            if mq:cnt+=1
print(cnt)