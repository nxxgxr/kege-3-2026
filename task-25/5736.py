def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num % i == 0 :
            d |= {i,num//i}
    if max(d) % 7 == 0:
        return max(d)
    return 0

cnt=0
for i in range(10**9+1,10**20):
    if str(i) == str(i)[::-1]:
        if g:=f(i):
            print(i,g)
            cnt+=1
            if cnt == 5:
                break
