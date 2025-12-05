from itertools import *

alph=sorted('гондубш')
cnt=0
for val in product(alph,repeat=6):
    cnt+=1
    slovo = ''.join(val)
    if slovo[0] != 'б' and slovo.count('н')>=2 and slovo.count('г=у') ==0:
            print(cnt)

