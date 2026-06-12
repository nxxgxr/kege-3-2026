def f(start,end,cnt=0):
    if start>end or cnt==2:return 0
    if start==end and cnt==1:return 1
    if start==30 or start==60:
        cnt+=1
    return f(start+1,end,cnt) + f(start*2,end,cnt) + f(start*3,end,cnt)

print(f(10,70))