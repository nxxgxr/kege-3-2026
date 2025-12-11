from itertools import product
from string import printable

cnt = 0

for val_tuple in product(printable[:16], repeat=4):
    val = ''.join(val_tuple)

    for i in range(len(val) - 1):
        if val[i] == val[i + 1]:
            break
    else:

        if val.count('3') == 1:
            if val[0]!='0':
                cnt += 1


print(cnt)