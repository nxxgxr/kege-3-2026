
ans=[]
for x in range(10,70001):
    sum = 5 ** 2025 + 5 ** 400 - x
    cnt=0
    while sum:
        if sum % 5 == 4:
            cnt+=1
        sum //=5
    ans.append((cnt,x))
print(max(ans))