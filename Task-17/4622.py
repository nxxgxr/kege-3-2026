with open(r'./files/17_4622.txt') as file:
    data=[int(x) for x in file]

minn=min(i for i in data if i > 0 and i%19==0)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=num1+num2 < minn
    if u1:
        ans+=[num1+num2]
print(len(ans),max(ans))