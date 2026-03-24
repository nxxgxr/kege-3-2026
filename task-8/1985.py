from itertools import permutations
alph=sorted('абиколун')
cnt=0
for val in permutations(alph,r=8):
    val=''.join(val)
    for i in val:
        if i in 'аиоу':
            val=val.replace(str(i),'*')
    for i in val:
        if i in 'бклн':
            val=val.replace(str(i),'!')
    if '**' not in val and '!!' not in val:
        cnt+=1
print(cnt)