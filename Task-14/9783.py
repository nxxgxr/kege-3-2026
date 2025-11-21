from string import printable as alph
for x in alph[:22]:
    sum1=int(f'18{x}89957',22)
    sum2=int(f'80{x}33',22)
    sum3=int(f'521{x}6',22)
    sum=sum1+sum2+sum3
    if sum%21==0:
        print(x,sum//21)
        break

