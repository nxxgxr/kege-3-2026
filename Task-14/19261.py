for x in range(0,36):
    num1=9*37**4 + 8*37**3 + x*37**2 + 3*37 + 1
    num2=1*37**4 + x*37**3 + 9*37**2 + 2*37 + 4
    sum=num1+num2
    if sum%21==0:
        print(sum//21)