def convert(num,sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1]


ans=[]
for n in range(1,100):
    r=convert(n,3)
    if n%3==0:
        r='1' + r + '02'
    else:
        g=convert(n%3 *5,3)
        r=r+g
    r=int(r,3)
    if r>=177:
        ans.append(n)
print(min(ans))







