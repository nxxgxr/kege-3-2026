from functools import *


def H(p): return p + 1, p * 2


@lru_cache(None)
def f(p):
    if p >= 129: return 'L'
    return 'W' if any(f(h) == 'L' for h in H(p)) else 'L'


@lru_cache(None)
def c(p):
    if p >= 129: return 0
    if f(p) == 'L': return 1 + max(c(h) for h in H(p))
    return 1 + min(c(h) for h in H(p) if f(h) == 'L')


# for s in range(1, 129):
#     if c(s) < 5: print(s, f(s), c(s))

print('19a:', min(s for s in range(1, 129) if c(s) == 2))
print('19б:', min(s for s in range(1, 129) if c(s * 2) == 1))
print('19в:', min(s for s in range(1, 129) if c(s) == 1))





