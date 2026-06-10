
with open(r'../files/26_7602.txt') as file:
    k=int(file.readline())
    n=int(file.readline())
    times=[list(map(int,i.split())) for i in file]

times=sorted(times)
cells=[0]*k

cnt=0
last_cell=0
for person in times:
    for i in range(k):
        if cells[i] < person[0]:
            cells[i]=person[1]
            last_cell = i + 1
            cnt+=1
            break
print(cnt,last_cell)