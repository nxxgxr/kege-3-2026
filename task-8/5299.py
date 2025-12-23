from itertools import *

cnt=0

for val in set(permutations('хочу сотку')):
    val=''.join(val)
    if val[0] not in ' у' and val[-1] != ' ' and  ' y' not in val:
        cnt+=1

print(cnt-1)