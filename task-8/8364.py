from itertools import *
alph=sorted('крате')
cnt=0
cnt2=0
cnt3=0
for val in product(alph,repeat=6):
    val=''.join(val)
    cnt+=1
    if val=='карета':
        cnt2+=cnt
    if val=='ракета':
        cnt3+=cnt
print(cnt3-cnt2-1)