from itertools import permutations


def f(x):
    b= 23 <= x <= 37
    c = 41 <= x <= 73
    a = a1 <= x <= a2
    return not(((not (b)) <= c ) <= a )

line=[x+eps for x in range(23,74) for eps in(0,0.1,0.9)]
ans=[]
for a1,a2 in permutations(line,2):
    if all( not f(x) for x in line):
        ans+=[a2-a1]
print(min(ans))