ans=[]

for x in range(1,1000):
    r=f'{x:b}'
    if x % 3 == 0:
        r+= r[-3:]
    else:
        r+= f'{(x%3)*3:b}'
    r=int(r,2)
    if r <= 170:
        ans.append(r)
print(max(ans))
