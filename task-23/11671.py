def f(start,end,cnt=0):
    cnt+=1
    if start==end:return 1
    if start>end:return 0
    return f(start+10,end,cnt) + f(start-5,end,cnt)

print(f(1,10,15))