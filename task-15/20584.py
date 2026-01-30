def d(n,m):
    return n%m==0

def f(x):
    return (d(405,x) <= d(81,x)) or (a-x > 162)

for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break


