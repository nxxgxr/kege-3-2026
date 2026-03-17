with open(r'./files/26_4712 (1).txt') as file:
    n=int(file.readline())
    boxes=[int(x) for x in file]

box=sorted(boxes,reverse=True)
ans = [box[0]]
for box in box[1:]:
    if ans[-1] - box >=3:
        ans+=[box]
print(len(ans),ans[-1])