def dl(n,m):
    return n%m==0
def f(x):
    return (dl(x,2)<=(not dl(x,3))) or (x+a>=100)

for a in range(1,2000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break