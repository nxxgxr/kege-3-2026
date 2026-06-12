
for x in range(10**6 *5 ,10**30):
    num=9**500 + 9**100 - x
    cnt8=0
    cnt4=0
    while num:
        if num%9==8:
            cnt8+=1
        if num%9==4:
            cnt4+=1
        num//=9
    print(x)
    if cnt8==90 and cnt4==2:
        print(x)
        break

#435848081
#10000000238
