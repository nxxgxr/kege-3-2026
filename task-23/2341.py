chet={1}
for i in range(8):
    chet={x+1 for x in chet} | {x+5 for x in chet} | {x *3 for x in chet}
cnt=0
for i in chet:
    if 1000<=i<=1024:
        cnt+=1
print(cnt)

# chet={1}
# for i in range(8):
#     chet={x+1 for x in chet if 1000<=x+1<=1024} | {x+5 for x in chet if 1000<=x+5<=1024} | {x *3 for x in chet if 1000<=x*3<=1024}
# print(len(chet))
