with open(r'./files/26_16390.txt') as file:
    s,n=map(int,file.readline().split())
    boxes=[int(x) for x in file]
boxes=sorted(boxes)
ans=[]
for i in boxes:
    if sum(ans) + i <=s:
        ans+=[i]
ans=ans[:-1]
boxes=sorted(boxes,reverse=True)
for i in boxes:
    if sum(ans) + i <=s:
        ans+=[i]
        break
print(len(ans),max(ans))

