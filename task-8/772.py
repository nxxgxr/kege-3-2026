from itertools import *
cnt=0
for val in permutations('пробник'):
    val=''.join(val)
    if (val[0] == ' п' or val[0]== 'р' or val[0]== 'б' or val[0]== 'н' or val[0]== 'к') and (val[-1] == ' п' or val[-1]== 'р' or val[-1]== 'б' or val[-1]== 'н' or val[-1]== 'к') and 'оо' not in val and 'ии' not in val:
        cnt+=1
print(cnt)