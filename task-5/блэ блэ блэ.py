for n in range(10000, 100000):
    o = str(n)
    square = (int(max(str(n))) + int(min(str(n)))) ** 2

    shet = 1
    for i in range(5):
        if int(o[i]) % 2 == 0:
            shet *= int(o[i])

    a = ''
    if square > shet:
        a = str(square) + str(shet)
    else:
        a = str(shet) + str(square)
    if a == '12116':
        print(n)
        break
