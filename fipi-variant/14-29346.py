from string import printable

def convert(num,sys):
    res=''
    while num!=0:
        res+=printable[num%sys]
        num//=sys
    return res[::-1]

num=convert(5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 -2025,36)
cnt=0
for i in num:
    if printable.index(i) %2==0:
        cnt+=1
print(cnt)