ans = []


def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(10, 100000):
    r = convert(n, 3)
    if n % 2 == 0:
        r += r[-2:]
    else:
        b = convert(sum(map(int, r)), 3)
        r += b
    r = int(r, 3)
    ans.append(r)
    b = min(ans)
    if b == 82:
        print(n)
        break
