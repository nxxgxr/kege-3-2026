from itertools import *
cnt=0
for val in set(permutations('амфибрахий')):
    val=''.join(val)
    if val[len(val) //2] == 'б' and val[len(val) //2 +1] == 'р':
        cnt+=1

print(cnt)
