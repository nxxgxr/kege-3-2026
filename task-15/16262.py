def f(x,y):
    return ((a<x) or (x**2 - 7*x + 10 > 0)) and ((a>=y) or (y**2 + 7*y + 12 >0))
cnt=0
for a in range(-50,50):
    if all(f(x,y) for x in range(-50,50) for y in range(-50,500)):
        cnt+=1
print(cnt)