with open(r'./26.txt') as file:
    n=int(file.readline())
    check_points={}
    for i in file:
        sportsman,point = map(int,i.split())
        if point not in check_points:
            check_points[point] = {sportsman}
        else:
            check_points[point] |= {sportsman}
ans=[]
for point in check_points:
    sort_sportsmen = sorted(check_points[point])
    cnt=1
    max_cnt=0
    for sp1,sp2  in zip(sort_sportsmen,sort_sportsmen[1:]):
        if sp2 - sp1 ==1:
            cnt+=1
        else:
            max_cnt=max(max_cnt,cnt)
            cnt=0
    max_cnt = max(max_cnt, cnt)
    ans+=[(max_cnt,point)]


print(min(i for i in ans if i[1]==max(ans)[1]))

