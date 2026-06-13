def f(s,e):
    if e>s or s==24:return 0
    if s==e:return 1
    return f(s-1,e) + f(s-4,e) + f(s//2,e)

print(f(34,30)*f(30,20)*f(20,9))