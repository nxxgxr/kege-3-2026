def f(num):
    for i in range(1,1000000):
        if i%2==1 and i%113==0:
            for g in range(1,13):
                if num == i + 3**g:
                    return g
    return 0


cnt=0
for i in range(100000,1000000):
    if str(i).count('0')==0:
        q=f(i)
        if f(i):
            print(i,q)
            cnt+=1
            if cnt==5:
                break
