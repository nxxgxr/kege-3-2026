def prost(num):
    if num<2:return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:return False
    return True
def f(num):
    d = set()
    cnt=0
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d)==3:
        for i in d:
            if prost(i):
                cnt+=1
        if cnt==3:
            return d
    return 0
cnt=0
for i in range(1_000_000,10**10):
    if f(i):
        print(i,f(i))
        cnt+=1
        if cnt==5:
            break
