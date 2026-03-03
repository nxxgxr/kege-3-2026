from itertools import *
def prost(num):
    if num < 2:return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True
ans=[]
for n in range(100, 1000):
    g = permutations(str(n),r=2)
    z=set()
    r=[]
    for p in g:
        p = ''.join(p)
        for q in p:
            if int(q)>2:
                z|={p}
    r=list(z)
    cnt=0
    for o in r:
        if prost(int(o)):
            cnt+=1
            ans.append((cnt,n))
print(max(ans))







