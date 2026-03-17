from functools import lru_cache
@lru_cache(None)
def f(start,end,cnt=0):
    if start==end:return cnt == 1
    if start>end:return 0
    if start in (24,32):
        cnt+=1
    if cnt>1:return 0
    return f(start+1,end,cnt) + f(start+2,end,cnt) + f(start+4,end,cnt) + f(start+8,end,cnt)

print(f(16,48))
