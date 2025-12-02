cnt2=0
for n in range(1,1000000):
    r=f'{n:x}'
    cnt=r.count('b')
    if cnt%2 ==0:
        r='1'+r
    else:
        r+='1'
    r=int(r,16)
    if 10<r<100:
        cnt2+=1

print(cnt2)