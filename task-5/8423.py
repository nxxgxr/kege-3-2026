def convert(num,sys):
    res=''
    while num!=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for n in range(10**4,10**7):
    r=convert(n,2)
    if n%5==0:
        r+=convert(5,2)
    else:
        r += convert(1, 2)

    if int(r,2) % 7==0:
        r += convert(7, 2)
    else:
        r += convert(1, 2)

    r=int(r,2)
    if r<1855663:
        ans+=[n]

print(max(ans))