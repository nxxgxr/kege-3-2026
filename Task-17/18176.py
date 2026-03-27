with open(r'./files/17_18176.txt') as file:
    data=[int(x) for x in file]
minn=min(x for x in data if str(x)[-1]=='4' and x>0)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=(sum(map(int,str(abs(num1)))) + sum(map(int,str(abs(num2)))) + sum(map(int,str(abs(num3))))) == minn
    if u1:
        ans+=[num1+num2+num3]


print(len(ans),max(ans))