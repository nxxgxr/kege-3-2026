from string import printable
for x in printable[:22]:
    num1=int(f'a23{x}ac0',22)
    num2=int(f'gb{x}21670',22)
    sum=num1+num2
    if sum % 21 ==0:
        print(x,sum//22)