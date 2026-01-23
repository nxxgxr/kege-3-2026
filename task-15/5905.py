def f(x,y,z):
    return (x | 50 ==0) or (y & 34 ==0) or (x*y*z > a // 8)

for a in range(1,200)[::-1]:
    if all(f(x,y,z) for x in range(1,200) for y in range(1,200) for z in range(1,200)):
        print(a)
        break