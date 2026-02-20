def f(start,end,pyt):
    pyt+=[start]
    if start==end and len(set(pyt))>52:return 1
    if start > end:return 0
    return f(start + 2,end,pyt) + f(start * 3,end,pyt) + f(start * 4,end,pyt)
print(f(2,400,[]))