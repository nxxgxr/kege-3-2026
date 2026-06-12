with open(r'files/17_16383.txt') as file:
    data=[int(x) for x in file]
maxx=max(x for x in data if len(str(abs(x)))==5 and str(x)[-2:]=='21')**2
ans=[]
for num1,num2 in zip(data,data[1:]):
    x1=len(str(abs(num1))) == 5 and str(num1)[-2:]=='21'
    x2=len(str(abs(num2))) == 5 and str(num2)[-2:]=='21'
    u1=x1 + x2 ==1
    u2= num1**2 + num2**2 >= maxx
    if u1+u2==2:
        ans+=[num1+num2]

print(len(ans),max(ans))
