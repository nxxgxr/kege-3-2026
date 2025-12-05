def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(13,100):
    sum1=7*100**6 + 10*100**5 +  x*100**4 +  0*100**3 +  1*100**2 + 2*100**1 + 3*100**0
    sum2=1*100**5 + 11*100**4 + 10*100**3 + 6*100**2 + 4*100**1 + x*100**0
    sum3=x*100**6+ 9*100**5 + 8*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + 12*100**0
    sum=sum1-sum2+sum3
    if sum%21==0:
        x=convert(x,6)
        print(x)

