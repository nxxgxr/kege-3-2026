def prost(num):
    if num<2:return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True

def dl(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    ans=[]
    for i in d:
        if prost(i):
            ans+=[i]
    if len(ans)>1:
        return sum(ans)
    return 0
cnt=0
for i in range(250000,10**10):
    f=dl(i)
    if f!=0 and f%17==0:
        print(i,f)
        cnt+=1
        if cnt==5:
            break