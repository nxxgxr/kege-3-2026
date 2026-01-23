
def f(x):
    p = x in range(2,21,2)
    q = x in range(3,31,3)
    a = x in As
    return (a<=p) and ((not q) <= (not a))
cnt=0
As=[]
for x in range(1,100):
    if not f(x):
        As.append(x)
print(len(As))




