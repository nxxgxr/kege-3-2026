from functools import *

@lru_cache(None)
def g(n):
    if n < 8: return 3*n
    return g(n-3) + 2

@lru_cache(None)
def f(n):return 3* (g(n-2) + 5)

for i in range(12346):
    g(i)

print(f(12345))