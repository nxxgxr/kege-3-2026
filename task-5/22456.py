ans=[]
for n in range(1, 1000000):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '11' + r[2:] + '1'
    else:
        b_nol = len(r) - r.count('1')
        if b_nol < r.count('1'):
            r += '0'
        else:
            r += '1'

    r = int(r, 2)
    if r > 271 :
        print(n)
        break


