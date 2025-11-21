from string import printable as alph
for X in alph[:20]:
    sum1=int(f'627{X}J8',20)
    sum2=int(f'H45I{X}5HIJ',20)
    sum3=int(f'4IDB49J{X}7',20)
    sum=sum1+sum2+sum3
    if sum%19==0:
        print(X,sum//19)