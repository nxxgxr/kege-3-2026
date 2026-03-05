def f(x,y,s):
    if x+y<=100:return s%2==0
    if s==0:return False
    h=[f(x-3,y-3,s-1),
       f(x//2,y,s-1),
       f(x,y//2,s-1)
    ]
    return any(h) if (s-1)%2==0 else all(h)
print("19:",[y for y in range(53,400) if f(48,y,2)][0])#59
print("20:",[y for y in range(53,400) if f(48,y,3) and not f(48,y,1)])
print("19:",[y for y in range(53,400) if f(48,y,4) and not f(48,y,2)][0])
