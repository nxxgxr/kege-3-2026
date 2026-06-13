with open(r'./files/17_21903.txt') as file:
    data=[int(x) for x in file]
minn=min(x for x in data if str(x)[-2:]=='15' and len(str(abs(x)))==3)**2
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=(num1>0 and num2>0 and num3>0) or (num1<0 and num2<0 and num3<0)
    u2= min(num1,num2,num3) * max(num1,num2,num3) > minn
    if u1+u2==2:
        ans+=[min(num1,num2,num3) * max(num1,num2,num3)]
print(len(ans),min(ans))