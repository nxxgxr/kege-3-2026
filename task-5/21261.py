def convert(num,sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans=[]
for n in range(1,1000000):
    r=convert(n,4)
    if sum(map(int,r)) % 3 == 0:
        r=r.replace('0','*')
        r=r.replace('2', '0')
        r=r.replace('*', '2')
        r= '32' + r
    else:
        r= r[0] + '10' + r[3:] + '33'
    r=int(r,4)
    if r > 320:
        ans.append([r,n])


min_r=min(ans)[0]
ans_2=[]
for i in ans:
    if i[0] == min_r:
        ans_2.append(i[1])

print(max(ans_2))
