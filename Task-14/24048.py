from string import printable as aph
for p in range(33,1000):
    num1=aph.index('k')*p**2 + aph.index('o')*p**1 + aph.index('t')
    num2=aph.index('g')*p**6 + aph.index('o')*p**5 + aph.index('l')*p**4 + aph.index('o')*p**3 + aph.index('d')*p**2 + aph.index('n')*p**1 + aph.index('i')
    num3 = aph.index('m')*p**4 + aph.index('e')*p**3 + aph.index('e')*p**2 + aph.index('o')*p**1 + aph.index('w')
    num4=1*p**2
    num5=20194023088
    sum=num1+num2-num3*num4+num5
    if sum==0:
        ans=aph.index('p')*p**3 + aph.index('u')*p**2 + aph.index('r')*p**1 + aph.index('r')*p**0
        print(ans)