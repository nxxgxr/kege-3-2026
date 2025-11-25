from string import printable as alph
for X in alph[:27]:
    sum1=int(f'8{X}38{X}68', 27)
    sum2=int(f'37{X}3163', 27)
    sum=sum1+sum2
    if sum%26==0:
        print(X,sum//26)