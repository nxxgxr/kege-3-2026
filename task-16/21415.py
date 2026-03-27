from functools import lru_cache
@lru_cache(None)
def f(n):
    if n<=5:return 1
    return n+ f(n-2)

for i in range(2,2200):
    f(i)

print(f(2126)-f(2122))