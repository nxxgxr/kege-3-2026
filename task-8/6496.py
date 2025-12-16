from itertools import *

alph='берск'
cnt5=0
cnt6=0
cnt7=0
for val in product(alph,repeat=5):
    slovo=''.join(val)
    cnt5+=1
for val in product(alph,repeat=6):
    slovo=''.join(val)
    cnt6+=1

for val in product(alph,repeat=7):
    slovo=''.join(val)
    cnt7+=1

print(cnt5+cnt6+cnt7)



