def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans=[]
for n in range(1, 100000):
    r = convert(n, 3)
    sum_1 = sum(map(int, r))
    if sum_1 % 3 == 0:
        r += '212'
    else:
        bbr = convert(sum_1 * 2,3)
        r+=bbr

    r=int(r,3)
    if r>490:
        ans.append(r)

print(min(ans))
