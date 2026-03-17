with open(r'./files/17_17558.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
cnt=len([1 for x in data if x%32==0])
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=num1<0
    u2=num2<0
    if u1+u2>=1:
        u3=num1+num2<cnt
        if u3:
            ans+=[num1+num2]

print(len(ans),max(ans))
