from itertools import *

cnt = 0
alph = 'зеркало'
for val in product(alph, repeat=6):
    slovo = ''.join(val)
    if 1<=slovo.count('к')<=4 and slovo.count('з')<2 and slovo.count('е')<2 and slovo.count('р')<2 and slovo.count('а')<2 and slovo.count('л')<2 and slovo.count('о')<2:
        cnt += 1
print(cnt)
