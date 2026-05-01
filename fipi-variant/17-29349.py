with open(r'./17_29349.txt') as file:
    data=[int(x) for x in file]
ans=[]
minn=min(x for x in data if abs(x)%123==0 and x>0)
for num1,num2 in zip(data,data[1:]):
    u1= num1+num2 < minn
    if u1:
        ans+=[num1+num2]

print(len(ans),max(ans))