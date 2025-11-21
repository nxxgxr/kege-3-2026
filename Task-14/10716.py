for x in range(1,150):
    sum1=5*150**4 + 1*150**3 + x*150**2 + 2*150 + 9
    sum2=x*150**3 + 2*150**1 + 3
    sum=sum1+sum2
    if sum % 149 == 0 :
        print(x,sum//149)