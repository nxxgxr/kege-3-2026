a=[]
for n in range(151,1000000):
    r=f'{n:x}'
    r=r.replace('a','1')
    cnt=0
    for chet in r:
        if chet in '2468ace':
            cnt+=1
    if cnt >2:
        r+='b'
    else:
        r='f'+r
    r=int(r,16)
    if r > 3500:
        a.append([r,n])
print(min(a))
