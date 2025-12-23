from itertools import *
alph='росмах'
cnt=0
for val in product(alph,repeat = 8):
    val=''.join(val)
    if val.count('р') == 1 and val.count('о') == 2 and val.count('с') == 1 and val.count('м') == 1 and val.count('а') == 2 and val.count('х') == 1:
        for i in 'рмсх':
            val = val.replace(i,'*')
        for i in 'оа':
            val =val.replace(i,'!')

        if '**' not in val and '!!' not in val:
            cnt+=1

print(cnt)