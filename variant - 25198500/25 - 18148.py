def dl(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    if d:
        return min(d)+max(d)
    else:
        return 0
cnt=0
for i in range(900_000,10**20):
    M=dl(i)
    if str(M)[-2:]=='46':
        print(i,M)
        cnt+=1
        if cnt==5:
            break
