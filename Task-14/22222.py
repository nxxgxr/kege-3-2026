sum_14=283**382 + 9**15 + 2**3

#b
cnt_B=0
while sum_14:
    if sum_14 % 14 == 11:
        cnt_B+=1
    sum_14 //=14

print(cnt_B)
sum_14=283**382 + 9**15 + 2**3
#
cnt_C=0
while sum_14:
    if sum_14 % 14 == 12:
        cnt_C+=1
    sum_14 //=14

print(cnt_C)