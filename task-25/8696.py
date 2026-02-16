def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0 :
            d |= {i,num//i}
    if len(d) > 1:
        return sum(d)
    return 0
cnt=0

for i in range(1_273_548,10**10):
    m=f(i)
    if f(i):
        if f(m % 100_000)==0:
            print(i,m)
            cnt+=1
            if cnt==5:
                break
