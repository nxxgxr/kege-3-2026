def fact(num):
    d=[]
    while num %2 ==0:
        d+=[2]
        num//=2
    i=3
    while i*i <= num:
        while num%i==0:
            d+=[i]
            num//=i
        i+=2
    if num > 2:
        d+=[num]
cnt=0
for n in range(5_000_012,10**20,100):
    d=fact(n)
    if any(d.count(i) == 5 for i in set(d)):
        print(n,min(i for i in set(d) if d.count(i)==5))
        cnt+=1
        if cnt==5:
            break



