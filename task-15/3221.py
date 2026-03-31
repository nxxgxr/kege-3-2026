def dl(x,y):
    return x%y==0

def f(x):
    return (dl(x,3) <= (not dl(x,5))) or (x+a>=70)

for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)
        break