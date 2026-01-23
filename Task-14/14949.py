from string import printable
for x in printable[:8]:
    num1=int(f'{x}1{x}',16)
    num2=int(f'{x}3{x}3',8)
    sum=num1+num2
    for i in range(1000):
        if 2**i==sum:
            print(x)

