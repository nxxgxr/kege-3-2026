with open(r'./files/17_6791.txt') as file:
    data=[int(x) for x in file]
minn=min(i for i in data if str(abs(i))[-2:]=='68')
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=str(abs(num1))[-2:]=='68'
    u2=str(abs(num2))[-2:]=='68'
    if u1+u2==1:
        u3= (num1 **2 + num2 **2) >= minn**2
        if u3:
            ans+=[num1**2 + num2**2]


print(len(ans),max(ans))