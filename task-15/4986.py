def f(x):
    b= 50 <= x <= 70
    return (x%a==0) or ((x%23==0) <= (not b ))

for a in range(1,10000):
    if all(f(x) for x in range(1,1000)):
        print(a)
