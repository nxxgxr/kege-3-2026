from itertools import *
alph='гепард'
cnt=0
for val in product(alph,repeat=5):
    slovo = ''.join(val)
    if slovo.count('г') == 1 and slovo[0] != 'а' and slovo[4] !='е':
        cnt+=1
print(cnt)