sum_9=729**8 - 3**18 + 85


cnt_9=0
while sum_9:
    if sum_9 % 9 == 0:
        cnt_9+=1
    sum_9 //=9

print(cnt)