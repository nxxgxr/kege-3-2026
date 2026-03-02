def f(start,end,a=0,b=0,c=0):
    if start==end and a>=2 and b<=4 and c==5: return 1
    if start>end: return 0
    return f(start*3,end,a+1,b,c) + f(start*5,end,a,b+1,c) + f(start+45,end,a,b,c+1)

print(f(1,2970))
