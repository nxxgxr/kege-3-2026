with open(r'./files/17_2473.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=num1 % 7==0
    u2=num2 % 7 ==0
    u3=str(num1)[-1]=='3'
    u4=str(num2)[-1]=='3'
    if (u1+u2 >=1) and (u3 + u4 >=1):
        ans+=[num1+num2]

print(len(ans),min(ans))

