for x in range(1,1000):
    r=f'{x:b}'
    if r.count('1') % 2 == 0:
        r='10' + r
    else:
        r= '1' + r +'01'
    r=int(r,2)
    if r < 30:
        print(x)
