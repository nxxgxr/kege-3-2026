def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    ans=[]
    if len(d)>=7:
        ans+=[sorted(d)[-7]]
        ans+=[len(d)]
        return ans
    return 0
cnt=0
for n in range(400_000_001,10**20):
    if G:=f(n):
        print(*G)
        cnt+=1
        if cnt==5:
            break





