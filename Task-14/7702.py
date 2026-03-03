ans=set()
for x in range(17):
    if x>8:
        a=x+1
    else:
        a=9
    for y in range(a,18):
        num1=5*18**3 + x*18**2 + y*18 + 10
        num2=1*y**3 + 8*y**2 + x*y + 7
        sum=num1+num2
        ans|={sum}
print(len(ans))