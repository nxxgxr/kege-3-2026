from functools import lru_cache

@lru_cache(None)
def f(n):
    if n>1: return n * f(n-1)
    return 1

for i in range(2100):
    f(i)

print( ( f(2024) - 5*f(2023)) / f(2022))
