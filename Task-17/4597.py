with open(r'.\files\17_4597.txt') as file:
    data = [int(x) for x in file]
m=min(data)
ans=[]
for i in range(len(data)-1):
    num1,num2= data[i:i+2]
    u1 = num1%117==m or num2%117==m
    if u1:
        ans+=[(num1+num2)]
print(len(ans),max(ans))


#################


with open(r'.\files\17_4597.txt') as file:
    data = [int(x) for x in file]
m=min(data)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1 = num1%117==m or num2%117==m
    if u1:
        ans+=[(num1+num2)]
print(len(ans),max(ans))