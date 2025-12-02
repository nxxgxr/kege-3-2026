from itertools import *

# product - функция, которая формирует
# все возможные комбинации символов длинной repeat
alph = 'PRIVET'
for val in product(alph,repeat=2):
    val=''.join(val)
    print(val)

# permutations - функция, которая формирует
# все возможные перестановки символов

for val in permutations(alph):
    val = ''.join(val)
    print(val)

# enumerate - нумерует элементы последовательности от start
res= enumerate(alph,start=1)
print(*res)