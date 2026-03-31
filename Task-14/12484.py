def f(num,sys):
    res=''
    while num!=0:
        res+=str(num%sys)
        num//=sys
    return res[::-1]
ans=[]
for x in range(1,1000):
    for y in range(1,1000):
        sum=(5**50) + (5**30) - 5**x - y - 5**y - x
        if sum>0:
            num=f(sum,5)
            if num.count('0')==10:
                ans+=[x*y]

print(max(ans))

