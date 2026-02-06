def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    m=0
    if len(d)>0:
        for i in d:
            m+=i
        m=int(m/(len(d)))
        if m%1000==313:
            return m
    return 0
cnt=0
for n in range(699_999,0,-1):
    if G:=f(n):
        print(n,G)
        cnt+=1
        if cnt==7:
            break


