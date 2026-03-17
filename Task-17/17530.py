with open(r'./files/17_17530.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
minn=min(data)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=num1%55==minn
    u2= num2%55==minn
    if u1+u2>=1:
        ans+=[num1+num2]

print(len(ans),min(ans))