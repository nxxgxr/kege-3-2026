from itertools import *
alph=sorted('ужемай')
cnt=0
ans=0
for val in product(alph,repeat=5):
    val=''.join(val)
    cnt+=1
    if 'уу' not in val and 'жж' not in val and 'ее' not in val and 'мм' not in val and 'аа' not in val and 'йй' not in val and cnt%2==0:
        ans+=1
print(ans)