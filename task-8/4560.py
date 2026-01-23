from itertools import *
alph=sorted('тихорецк')
cnt=0
for val in permutations(alph,r=4):
    val=''.join(val)
    aaa=0
    if (val.count("и")+val.count("о")+val.count("е"))==2:
        for i in range(4):
            if val[i]=='тихо'[i]:
                aaa+=1
        if aaa==2:
            cnt+=1

print(cnt)