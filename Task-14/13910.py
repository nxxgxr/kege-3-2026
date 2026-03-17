from string import printable as alph


for p in range(31,37):
    num1=alph.index('t') * p + alph.index('h')
    num2=alph.index('n')*p + alph.index('q')
    num3=alph.index('u')
    num4=1*p**2 + alph.index('l')*p + 7
    sum=num1+num2+num3-num4
    if sum==0:
        print(p)