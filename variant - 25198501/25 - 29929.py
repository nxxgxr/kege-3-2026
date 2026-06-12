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
    while i ** 2 <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    if len(d) == 2 and len(set(d)) == 2:
        if all(1 for x in d if prost(x)):
            for i in range(min(d) + 1, max(d)):
                if prost(i):
                    return 0
            return sum(d)
    else:
        return 0


cnt = 0
for i in range(3_700_001, 10 ** 200):
    m = mn(i)
    if m:
        print(i, m)
        cnt += 1
        if cnt == 5:
            break
