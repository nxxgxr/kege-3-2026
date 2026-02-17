def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d= set()
    prost=[]
    for i in range(2,int(num**.5)+1):
        if num % i ==0:
            d|={i,num//i}
    for i in d:
        if is_prime(i):
            prost+=[i]
    if len(prost) >=4:
        return sorted(prost)[0] + sorted(prost)[1] + sorted(prost)[-1] + sorted(prost)[-2]
    return 0
cnt=0
for n in range(456_790,10**20):
    m=f(n)
    if m % 114 == 39:
        print(n,m)
        cnt+=1
        if cnt==5:
            break
