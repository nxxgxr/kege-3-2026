def f(x,y,s):
    if x+y<=108:return s%2==0
    if s==0:return False
    h=[f(x-2,y,s-1),
       f((x+1)//2,y,s-1),
       f(x,y-2,s-1),
       f(x,(y+1)//2 ,s-1)]
    return any(h) if (s-1)%2==0 else all(h)
print('19:',[y for y in range(500,1,-1) if f(60,y,2)][0])#192
print('19:',[y for y in range(500,1,-1) if f(60,y,3) and not f(60,y,1)][:2])#99 196
print('19:',[y for y in range(500,1,-1) if f(60,y,4) and not f(60,y,2)][0])