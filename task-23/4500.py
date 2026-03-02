from functools import *
@lru_cache(None)
def f(start,end,a=[]):
    if start==end:return 1
    if start>end or start==23:return 0
    if a[-1]=='1':
        f(start+2,end,a+[0]) + f(start*2,end,a+[0])
    return f(start+1,end,a+[1]) + f(start+2,end,a+[0]) + f(start*2,end,a+[0])
print(f(3,11)*f(11,79))