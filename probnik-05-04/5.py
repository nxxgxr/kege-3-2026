def convert(num,sys):
    res=''
    while num!=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for n in range(1,1000):
    r=convert(n,4)
    if n%4==0:
        r=str(r)[:2] + r
    else:
        r=r + str(convert(((n%4) * 4),4))
    r=int(r,4)
    if r>291:
        ans+=[r]


print(min(ans))


