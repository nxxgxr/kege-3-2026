def prime(num):
    d=[]
    while num % 2 ==0:
        d+=[2]
        num //=2
    i=3
    while i*i <= num:
        while num%i==0:
            d+=[i]
            num//=i
        i+=2
    if num > 2:
        d += [num]
    return d
cnt=0
for i in range(13_475_125,10**20):
    g=prime(i)
    if len(g) == 5:
        if all('5' in str(num) for num in g):
            print(i,max(g))
            cnt+=1
            if cnt==5:
                break
