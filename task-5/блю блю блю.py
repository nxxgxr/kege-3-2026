k=0
for n in range(1,1000):
    r=f'{n:b}'
    if n%8==0:
        r+=r[-2:]
    else:
        b=f'{(n%8)*2:b}'
        r+=b
    r=int(r,2)
    if r>3000:
        print(n)
        break