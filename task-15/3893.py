def d(x,y):
    return abs(x) % abs(y)==0
def f(x):
    return d(a,25) and ( (d(x,24) and d(x,75)) <= d(x,a)  )
cnt=0
for a in range(-5000,-1):
    if all(f(x) for x in range(-7000,7000)):
        cnt+=1
for a in range(1,6000):
    if all(f(x) for x in range(-7000,7000)):
        cnt+=1
print(cnt)


