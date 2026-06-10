ans=[]
for n in range(1,16):
    r=f'{n:b}'
    if r.count('1') % 2==0:
        r= '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'
    r=int(r,2)
    ans+=[r]
print(max(ans))
