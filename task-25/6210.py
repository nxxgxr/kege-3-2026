from fnmatch import fnmatch
def f(num):
    d=set()
    for i in range(1,int(num**.5)+1):
        if num % i==0:
            d |= {i,num//i}
    return d
for i in range(22 - 22%53,10**7, 53):

    if f(i):
        if str(i) == str(i)[::-1]:
            if len(f(i)) > 30:
                if fnmatch(str(i),'*2?2*'):
                    print(i,sum(f(i)))

