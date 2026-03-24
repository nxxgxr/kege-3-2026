def f(x,y,s):
    if x*y>384:return s%2==0
    if s==0:return False
    h=[f(x+5,y,s-1),
       f(x,y+5,s-1),
       f(x*2,y,s-1),
       f(x,y*2,s-1)
    ]
    return any(h) if (s-1)%2==0 else all(h)

print('19:',[y for y in range(1,55) if f(8,y,2)][0])#13
print('19:',[y for y in range(1,55) if f(8,y,3) and not f(8,y,1)])
print('19:',[y for y in range(1,55) if f(8,y,4) and not f(8,y,2)][0])