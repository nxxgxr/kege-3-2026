def dig(x,y):
    a=f'{x}'
    b=f'{y}'
    if a[0]==b[0]:return True
    return False

def f(x):
    return ((not(dig(x,28))) and dig(x,47)) <= (x > a -20)

for a in range(10000,1,-1):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break
