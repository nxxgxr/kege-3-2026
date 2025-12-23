from itertools import *

alph='ворота'


cnt=0
for val in set(permutations(alph,r = 6)):
    val=''.join(val)
    if 'оо' not in val and 'оa' not in val and 'ао' not in val:
        cnt+=1
print(cnt)