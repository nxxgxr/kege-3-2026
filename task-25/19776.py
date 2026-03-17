def prost(num):
    if num<2:return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True

def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    ans=[]
    for i in d:
        if prost(i):
            ans+=[i]
    if len(ans)>=2:
        return min(ans) + max(ans)

cnt=0
for i in range(23_600_000,10**20):
    m=f(i)
    if m:
        if m % 213 == 171:
            print(i,m)
            cnt+=1
            if cnt==6:break