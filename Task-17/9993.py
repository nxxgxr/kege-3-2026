with open(r'./files/17_9993.txt') as file:
    data=[int(x) for x in file]

def prost(x):
    if x<2:return False
    for i in range(2,int(x**.5)+1):
        if x%i==0:
            return False
    return True

maxx=max(int(x) for x in data if str(x)[-2:]=='17')
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=prost(num1) + prost(num2) == 1
    u2=(abs(num1+num2) % abs(maxx))==0
    if u1+u2==2:
        ans+=[num1*num2]

print(len(ans),max(ans))
