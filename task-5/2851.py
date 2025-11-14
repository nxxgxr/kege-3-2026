
for n in range(2,10000):
    r = f'{n:b}'
    x=r[1::2].count('1')
    y=r[::2].count('0')
    r =  abs(x - y)
    if r == 5:
        print(n)
        break



