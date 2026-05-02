with open(r'./files/26_20815.txt') as file:
    n,S= map(int,file.readline().split())
    data=[]
    for i in file:
        id,e1,e2,e3,s=map(int,i.split())
        data.append([e1+e2+e3+s,s,id])

astronauts=sorted(data,key=lambda x: (-x[0],-x[1],x[2]))

passed=astronauts[:S]
rejected=astronauts[S:]
half_points=passed[-1][0]


print([i[2] for i in passed if i[0]!=half_points][-1])
print(sum(1 for i in astronauts if i[0]==half_points))