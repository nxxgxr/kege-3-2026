
from itertools import permutations


def f(x):
    p= 16 <= x <= 84
    q = 27 <= x <= 43
    a = a1 <= x <= a2
    return (a<=p) or q

line=[x+eps for x in range(16,85) for eps in (0,0.1,0.9)]

ans=[]
for a1,a2 in permutations(line,2):
    if all(f(x) for x in line):
        ans+=[a2-a1]

print(max(ans))

