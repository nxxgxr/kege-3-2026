def convert(num,sys):
    res=''
    while num !=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]

ans=[]
for n in range(1,100000):
    r=convert(n,3)
    if n % 3 == 0:
        r+=r[-2:]
    else:
        r+=convert(3*sum(map(int,r)),3)
    r=int(r,3)
    if r>208 and r%2==1:
        ans.append(r)
print(min(ans))

