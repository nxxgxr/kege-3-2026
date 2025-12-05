from itertools import *

alph = sorted('солнце')
cnt = 0
ans=0
for val in product(alph, repeat=6):
    cnt+=1
    slovo = ''.join(val)
    if slovo[0] not in "ое" and cnt % 2 ==0 and slovo.count('ц')==2:
        ans+=1
print(ans)