def fact(num):
    d=[]
    while num % 2 == 0:
        d+=[2]
        num//=2
    i=3
    while i**2 <= num:
        while num % i ==0:
            d+=[i]
            num//=i
        i+=2
    if num > 1 :
        d+=[num]
    return d

cnt=0
for i in range(7_305_679,10**20):
    g=sum(fact(i))
    if len(fact(i)) == 4:
        if str(g) == str(g)[::-1]:
            print(i,g)
            cnt+=1
            if cnt==5:
                break

