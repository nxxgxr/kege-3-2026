def tr(f,m,k):
    return f+m>k and f+k>m and m+k>f

def f(x):
    return not((tr(x,11,18)==(not(max(x,5)>68))) and tr(x,a,5))
for a in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(a)


