def convert(num,sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for n in range(1,2000):
    r=convert(n,2)
    r=r[1:]
    if r.count('1')%2==0:
        r='10'+r
    else:
        r='1' + r + '0'
    r=int(r,2)
    if r<450:
        ans+=[r]
print(max(ans))