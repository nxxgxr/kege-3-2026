def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d=set()
    for i in range(2,int(num**.5) +1):
        if num%i==0 and i % 10 == 7:
            d|={i}
        if num%i==0 and num//i % 10 == 7:
            d|={num//i}
    prost=[]
    for i in d:
        if is_prime(i):
            prost+=[i]
    if len(prost) > 0:
        return (sum(prost)) // len(prost)
    return 0
cnt=0
for n in range(749_999,0,-1):
    s=f(n)
    if s!=0 and s%111 == 0:
        print(n,s)
        cnt+=1
        if cnt==5:
            break
