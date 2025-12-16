from itertools import *
alph='моль'
cnt=0
for val in product(alph,repeat=5):
    slovo=''.join(val)
    if slovo.count('оь') == 0 and slovo[0]!='ь' and 'ьь' not in slovo:
        cnt+=1
        print(slovo)
print(cnt)
