def DEL(n, m):
    return n % m == 0
print(263*71)
def f(x):
    return not(DEL(x, 263) <= DEL(x,a)) and (DEL(x,71))

for a in range(20000,1,-1):
    if all(not f(x) for x in range(1, 100000)):
        print(a)
        break


