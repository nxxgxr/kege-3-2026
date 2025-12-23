from itertools import *

alph=sorted('сентябрь')
cnt=0
for val in product(alph,repeat = 5):
    val=''.join(val)
    cnt+=1
    if val[0] == 'р' and val.count('ь')==0:
        print(cnt)