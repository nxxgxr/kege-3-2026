from string import printable
def f(num):
    res = ''
    while num != 0:
        res += str(printable[num % 39])
        num //= 39
    return res[::-1]
ans=[]
for x in range(1,9430):
    sum=39**483 + 39**235 -x
    num=f(sum)
    ans+=[num.count('0')]
print(max(ans))





