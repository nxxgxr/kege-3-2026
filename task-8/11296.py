from itertools import *

alph = sorted('досж')
cnt = 1
for val in product(alph, repeat=6):
    slovo = ''.join(val)
    if slovo[0:2] == 'жс':
        print(slovo)
        print(cnt)
        break
    cnt += 1