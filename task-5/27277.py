def convert(num,sys):
    res=''
    while num != 0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
for n in range(1,1000):
    r=convert(n,3)
    if n%3 != 0:
        r='1' + r + str(r)[-3:]
    else:
        g=convert( (sum(map(int,r))) * 8, 3)
        r+=g
    r=int(r,3)
    if 1204<r<1236:
        print(r)
