def convert(num,sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for n in range(167,10000):
    r=convert(n,3)
    s=sum(map(int,r))
    if s % 9==0:
        r+='2'
    else:
        r+=str(convert(s%9,3))
    r=int(r,3)
    ans+=[r]
print(min(ans))