for x in range(1,1000):
    r=f'{x:b}'
    if r.count('1') % 2 ==0:
        r='10' + r[2:] + '0'
    else:
        r= '11' + r[2:] + '1'
    r= int(r,2)
    if r <35:
        print(r,x)
