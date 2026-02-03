def is_prime(num):
    if num < 2: False
    for i in range(2,int(num**.5)+1):
        if num%i==0: return False
    return True

def f(num):
    d=set()
    for i in range(2,int(num**.5)+1):
        if num % i ==0:
            if is_prime(i): d|={i}
            if is_prime(num//i): d|={num//i}
    if len(d) > 1:
        M=min(d) + max(d)
        if str(M)==str(M)[::-1] and M>60_000:
            return M
    return 0

cnt=0
for n in range(5_400_000,10**20):
    if G:=f(n):
        print(n,G)
        cnt+=1
        if cnt==5:
            break
