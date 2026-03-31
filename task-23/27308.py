def f(start,end,cnt=0):
    if start<end:return 0
    if start==18 or start==38:
        cnt+=1
    if start==end and cnt>=1:return 1
    return f(start-3,end,cnt) + f(start-5,end,cnt) + f(start//3,end,cnt)

print(f(80,3))

