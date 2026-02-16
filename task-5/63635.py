ans=[]
for n in range(1,10000):
    r=f'{n:b}'
    g=sum(map(int,r)) % 2
    r+= str(g)
    g = sum(map(int, r)) % 2
    r += str(g)
    r=int(r,2)
    if r > 73:
        ans+=[r]
print(min(ans))

