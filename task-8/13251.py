from itertools import *
cnt=0
alph='кайф'
for val in product(alph,repeat=4):
    val=''.join(val)
    if len(set(val))==4 and val[-1]!='й' and 'кф' not in val:
        cnt+=1
print(cnt)