with open(r'./files/17_1970.txt') as file:
    qw=[int(x) for x in file]

ans=[]
for num1,num2 in zip(qw,qw[1:]):
    u1=num1%3==0 or num2%3==0
    if u1:
        ans+=[num1+num2]
print(len(ans),max(ans))