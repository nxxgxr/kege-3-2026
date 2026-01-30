from itertools import *
alph=sorted('аекнс')
cnt=0
for val in product(alph,repeat=6):
    val=''.join(val)
    cnt+=1
    if val=='сенека':
        print(cnt)