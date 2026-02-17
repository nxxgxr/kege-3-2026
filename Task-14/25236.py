for p in range(36,11,-1):
    for x in range(1,500001):
        num=int(f'29a1',p)+int(f'47771',p)+int(f'12a',p)-1000000-x
        if num==0:
            print(p)
            break
