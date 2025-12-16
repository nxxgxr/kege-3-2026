from itertools import *
alph=sorted('январь')
cnt=0
for val in product(alph,repeat=5):
    slovo=''.join(val)
    if slovo[-1] != 'я' and slovo.count('ь') <2 and slovo.count('яя') == 0:
        print(slovo)
        cnt+=1
print(cnt)
