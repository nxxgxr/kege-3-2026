from itertools import *
alph=sorted('нормалье')
cnt=0
cnt1=[]
cnt2=0
for val in product(alph, repeat=6):
    val = ''.join(val)
    cnt+=1
    if val[:4]=='норм':
        cnt1.append(cnt)
    if val[:6]=='ненорм':
        cnt2=cnt


print(abs(cnt2-min(cnt1))-1)
