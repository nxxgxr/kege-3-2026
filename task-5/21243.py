def convert(num,sys):
    res=''
    while num!=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for n in range(1,1000):
    r=convert(n,5)
    if sum(map(int,r)) % 5 ==0:
        r=r.replace('0','*')
        r=r.replace('1','0')
        r=r.replace('*','1')
        r+='14'
    else:
        r+='33'
        r='44' + str(r)[2:]
    r=int(r,5)
    if r==384:
        ans+=[n]
print(min(ans))