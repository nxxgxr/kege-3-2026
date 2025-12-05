from itertools import *

cnt = 0
alph = 'пскаль'
for val in product(alph, repeat=4):
    slovo = ''.join(val)
    if slovo[0] != 'ь' and slovo.count('ьь') == 0 and slovo.count('ььь') == 0 and slovo.count('ьььь')==0:
        cnt += 1
print(cnt)
