from itertools import *
alph= 'джаваскрипт'
cnt=0
for val in set(permutations(alph)):
    val=''.join(val)
    poz=0
    for i in range(len(val)):
        if val[i] in 'аи':
            poz+=i + 1
    if poz==11:
        cnt+=1
print(cnt)