def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]



for n in range(11, 1000000):
    r = convert(n, 3)
    h = 0
    j = 0
    for i in r:
        if int(i) % 2 == 0:
            h += 1
        else:
            j += 1

    if h > j:
        r = '22' + r
    else:
        r = '11' + r

    R = int(r, 3)

    if R > 100:
        print(R)
        break


