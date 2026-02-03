ans=[]
for n in range(1,10000):
    r=bin(2+n)[2:]
    g=sum(map(int,r)) % 2
    r+=str(g)
    r+=str(sum(map(int,r)) % 2)
    r=int(r,2)
    if r<61:
        ans.append(n)
print(max(ans))
