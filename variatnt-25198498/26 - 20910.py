with open(r'./files/26_20910.txt') as file:
    n,m,k = map(int,file.readline().split())
    ryad=[list(map(int,i.split())) for i in file]

ryad=sorted(ryad)
for x in range(21000,m):
    zmest=[q[1] for q in ryad if q[0] < x]
    for y in range(1,k):
        if y not in zmest and y+1 not in zmest:
            print(x,y,y+1)
            break

