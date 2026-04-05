def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            d|={i,num//i}
    ans=[]
    for i in d:
        if i!=11 and str(i)[-2:] =='11':
            ans+=[i]
    if len(ans)>0:
        return min(ans)
    return 0
cnt=0


for i in range(1_350_050,10**10):
    bla = f(i)
    if bla:
        print(i,bla)
        cnt+=1
        if cnt==5:
            break