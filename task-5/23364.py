def convert(num,sys):
    res=''
    while num != 0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for n in range(1,10000):
    r=convert(n,3)
    if n % 3==0:
        r= '1' + r +'02'
    else:
        g=convert(n%3 * 4,3)
        r+=g
    r=int(r,3)
    if r <=100:
        ans+=[n]
print(max(ans))
