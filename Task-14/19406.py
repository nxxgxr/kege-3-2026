from string import printable as alph

for x in alph[1:35]:
    n1=int(f'6{x}qr{x}',35)
    n2=int(f'{x}59sh',35)
    n3=int(f'ph{x}69yw',35)
    num=str(n1+n2+n3)
    num2=n1+n2+n3
    bykva=0
    raz=0
    bbr=[]
    for y in num:
        raz=num.count(y)
        bykva = y
        bbr.append([raz,bykva])
    mx=max(bbr)[1]
    otv=int(mx)
    if num2 % int(mx) == 0:
        print(num2//(otv*otv))


