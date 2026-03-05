def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans=set()


for a in range(625,3125):
    for b in range(625,a):
        qc = a - b
        c = convert(qc,5)
        if len(c) == 5:
            ans|={c}
print(len(ans))