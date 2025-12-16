from string import printable as alph

for x in alph[:25]:
    sum1=int(f'a4{x}7f2',25)
    sum2=int(f'n{x}g5{x}h',25)
    sum3=int(f'74{x}m26',25)
    sum=sum1+sum2+sum3
    if sum % 24==0:
        print(x,sum//24)
