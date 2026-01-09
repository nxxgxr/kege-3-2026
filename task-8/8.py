from itertools import *
from string import printable

alph = printable[:25]
cnt = 0


ans = []

for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        nechet = 0
        pyat = 0
        for i in range(len(val)):
            g = alph.index(val[i])
            if g % 2 == 1:
                nechet += 1
            if g <= 5:
                pyat += 1
        if nechet == 1 and pyat <= 2:
            cnt += 1

print(cnt)
