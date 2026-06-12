def f(s,e):
    if e>s or s==24:return 0
    if s==e:return 1
    return f(s-1,e) + f(s-6,e) + f(s//2,e)

print(f(34,29) * f(29,19) * f(19,6))