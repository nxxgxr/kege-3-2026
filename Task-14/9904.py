from string import printable as alph
g=[]
for y in range(9,13):
    for x in range(y+1,14):
        sum1=int(f'7{alph[x]}37{alph[y]}', 14)
        sum2=int(f'9{alph[y]}63',x)
        sum3=int(f'15148',y)
        sum=sum1+sum2-sum3
        g.append(sum)
        if sum == 316323:
            print(sum, x, y, (sum // (x + y)))
            break


