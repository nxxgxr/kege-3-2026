from string import printable
from itertools import *

alph = printable[:12]
cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in range(len(val) - 1): # 45
            if int(val[i], 12) % 3 == 0 and int(val[i + 1], 12) % 3 == 0 or \
                    int(val[i], 12) % 3 != 0 and int(val[i + 1], 12) % 3 != 0:
                break
        else:
            cnt += 1
print(cnt)