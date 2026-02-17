from itertools import *
cnt=0
alph='просто'
for val in set(permutations(alph,r=6)):
    val=''.join(val)
    if 'оо' not in val:
        cnt+=1
        print(val)
print(cnt)
