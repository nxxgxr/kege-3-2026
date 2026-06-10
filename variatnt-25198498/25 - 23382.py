def prost(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def mn(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    cnt = 0
    if len(d) == 2:
        for i in d:
            if prost(i) and str(i).count('2') == 1: cnt += 1
    if cnt == 2:
        return max(d)
    return 0
cnt = 0
for i in range(6_651_220, 10 ** 20):
    M = mn(i)
    if M:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break
