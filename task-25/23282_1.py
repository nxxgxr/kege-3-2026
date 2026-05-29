def prost(num):
    if num<2: return False
    for i in range(2,int(num**.5)+1):
        if num%i==0: return False
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
    if len(ans)>1:
        return min(ans)+max(ans)
    else:
        return 0


cnt=0
for i in range(5_400_001,10**20):
    M=f(i)
    if M>60_000 and str(M)==str(M)[::-1]:
        print(i,M)
        cnt+=1
        if cnt==5:
            break


