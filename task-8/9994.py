from itertools import *
cnt=0
alph=sorted('школа')
for val in product(alph,repeat=5):
    val=''.join(val)
    cnt+=1
    if val=='шалаш':
        print(cnt)