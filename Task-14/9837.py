from string import printable as alph

for x in alph[:23]:
    sum1=int(f'7{x}38596',23)
    sum2=int(f'14{x}36',23)
    sum3=int(f'61{x}7',23)
    sum=sum1+sum2+sum3
    if sum % 22==0:
        print(x,sum//22)
        break