from itertools import *

alph = sorted('аожпюз')
cnt = 0
num = 0

for val in product(alph, repeat=6):
    num += 1
    slovo = ''.join(val)
    if slovo[0] == 'а' and slovo.count('з') >= 2 and num % 2 == 0:
        cnt += 1

print(cnt)