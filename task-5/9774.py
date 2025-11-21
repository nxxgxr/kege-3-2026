def convert(num,sys):
    res=''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans=[]
for x in range(1,100000):
    r= convert(x,3)
    if x % 3 == 0:
        r= r + r[-2:]
    else:
        r= r+ convert(x%3*5,3)
    r=int(r,3)
    if r > 133:
        ans.append(r)
print(min(ans))