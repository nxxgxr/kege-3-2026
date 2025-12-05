from itertools import *

cnt = 0
alph = 'ничья'
for val in product(alph, repeat=7):
    slovo = ''.join(val)
    if slovo.count('ии') == 0 and slovo.count('яя') == 0 and slovo.count('яи') == 0 and slovo.count('я') and ((slovo.count('и') + slovo.count('я'))==2) :
        cnt += 1
print(cnt)
